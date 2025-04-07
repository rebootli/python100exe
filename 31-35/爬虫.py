
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import json
import random
import os

class DongchediSeleniumCrawler:
    def __init__(self, edgedriver_path=None):
        self.base_url = "https://www.dongchedi.com"
        self.setup_driver(edgedriver_path)
        self.car_data = []
    
    def setup_driver(self, edgedriver_path=None):
        """设置Selenium WebDriver"""
        options = Options()
        # options.add_argument("--headless")  # 先不使用无头模式，方便调试
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # 添加忽略SSL错误的选项
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--allow-insecure-localhost")
        # 添加WebGL相关选项
        options.add_argument("--enable-unsafe-swiftshader")
        options.add_argument("--disable-web-security")
        
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.178 Safari/537.36 Edg/134.0.6998.178")
        
        # 使用本地EdgeDriver路径
        if edgedriver_path and os.path.exists(edgedriver_path):
            self.driver = webdriver.Edge(service=Service(edgedriver_path), options=options)
        else:
            # 如果没有提供路径，尝试使用默认方式
            try:
                self.driver = webdriver.Edge(options=options)
            except Exception as e:
                print(f"初始化Edge驱动失败: {e}")
                print("请下载与您Edge浏览器版本匹配的EdgeDriver，并提供路径")
                raise
        
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(30)
        # 设置脚本执行超时时间
        self.driver.set_script_timeout(30)
        
        self.wait = WebDriverWait(self.driver, 15)  # 增加等待时间
    
    def get_car_list_page(self, page=1):
        """获取汽车列表页"""
        # 懂车帝车型库页面URL
        url = f"{self.base_url}/auto/series/list"
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                print(f"尝试获取列表页，第 {retry_count + 1} 次尝试...")
                self.driver.get(url)
                
                # 等待页面加载
                time.sleep(5)  # 先等待一段时间让页面基本加载
                
                # 尝试查找页面上的一些基本元素，确认页面已加载
                try:
                    # 先尝试查找页面标题或其他常见元素
                    self.driver.find_element(By.TAG_NAME, "body")
                    print("页面基本元素已加载")
                    
                    # 尝试多种可能的选择器
                    selectors = [
                        ".series-card", 
                        ".car-item", 
                        ".car-series-item", 
                        "[class*='series']", 
                        "[class*='car-']"
                    ]
                    
                    element_found = False
                    for selector in selectors:
                        try:
                            WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                            )
                            print(f"找到车型元素，使用选择器: {selector}")
                            element_found = True
                            break
                        except Exception:
                            continue
                    
                    if not element_found:
                        print("未找到车型元素，尝试查看页面源码")
                        # 打印页面源码的一部分，帮助调试
                        page_source = self.driver.page_source
                        print(f"页面源码片段: {page_source[:500]}...")
                        
                        # 尝试截图保存
                        try:
                            screenshot_path = f"d:\\TRAE\\爬虫\\page_screenshot_{page}.png"
                            self.driver.save_screenshot(screenshot_path)
                            print(f"页面截图已保存至: {screenshot_path}")
                        except Exception as ss_e:
                            print(f"截图失败: {ss_e}")
                except Exception as e:
                    print(f"页面基本元素加载失败: {e}")
                
                # 如果需要翻页，可以在这里添加翻页逻辑
                if page > 1:
                    # 查找并点击翻页按钮，具体选择器需要根据实际页面调整
                    try:
                        next_page_btn = self.driver.find_element(By.XPATH, f"//a[contains(@class, 'pagination-item') and text()='{page}']")
                        next_page_btn.click()
                        time.sleep(2)  # 等待页面加载
                    except Exception as e:
                        print(f"翻页失败: {e}")
                
                return True
            except Exception as e:
                retry_count += 1
                print(f"获取列表页失败 (尝试 {retry_count}/{max_retries}): {e}")
                time.sleep(3)  # 等待一段时间后重试
        
        print(f"获取列表页失败，已达到最大重试次数 {max_retries}")
        return False
    
    def parse_car_list(self):
        """解析汽车列表页，提取车辆信息和详情页链接"""
        car_links = []
        try:
            # 尝试多种可能的选择器
            selectors = [
                ".series-card", 
                ".car-item", 
                ".car-series-item", 
                "[class*='series']", 
                "[class*='car-']"
            ]
            
            car_items = []
            for selector in selectors:
                try:
                    items = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if items:
                        print(f"使用选择器 '{selector}' 找到 {len(items)} 个元素")
                        car_items = items
                        break
                except Exception as e:
                    print(f"选择器 '{selector}' 查找失败: {e}")
            
            print(f"找到 {len(car_items)} 个车型卡片")
            
            if not car_items:
                # 如果没有找到车型卡片，尝试直接查找所有链接
                print("尝试查找所有链接...")
                all_links = self.driver.find_elements(By.TAG_NAME, "a")
                for link in all_links:
                    try:
                        href = link.get_attribute("href")
                        if href and "/auto/series/" in href:
                            car_links.append(href)
                            print(f"找到车型链接: {href}")
                    except Exception:
                        continue
            else:
                # 如果找到了车型卡片，从中提取链接
                for item in car_items:
                    try:
                        # 尝试多种方式获取链接
                        link_found = False
                        
                        # 方式1: 直接查找a标签
                        try:
                            link_elements = item.find_elements(By.TAG_NAME, "a")
                            for link_element in link_elements:
                                href = link_element.get_attribute("href")
                                if href and "/auto/series/" in href:
                                    car_links.append(href)
                                    print(f"找到车型链接: {href}")
                                    link_found = True
                                    break
                        except Exception as e:
                            print(f"方式1查找链接失败: {e}")
                        
                        # 方式2: 如果方式1失败，尝试获取整个元素的点击链接
                        if not link_found:
                            try:
                                href = item.get_attribute("onclick")
                                if href and "location.href" in href:
                                    # 提取链接
                                    import re
                                    match = re.search(r"location\.href='([^']+)'", href)
                                    if match:
                                        extracted_href = match.group(1)
                                        if "/auto/series/" in extracted_href:
                                            car_links.append(extracted_href)
                                            print(f"找到车型链接(方式2): {extracted_href}")
                                            link_found = True
                            except Exception as e:
                                print(f"方式2查找链接失败: {e}")
                    except Exception as e:
                        print(f"解析车辆链接失败: {e}")
        except Exception as e:
            print(f"解析列表页失败: {e}")
        
        return car_links
    
    def get_car_detail(self, url):
        """获取汽车详情页"""
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                print(f"尝试获取详情页 {url}，第 {retry_count + 1} 次尝试...")
                self.driver.get(url)
                
                # 等待页面加载
                time.sleep(5)  # 先等待一段时间让页面基本加载
                
                # 尝试查找页面上的一些基本元素，确认页面已加载
                try:
                    # 先尝试查找页面标题或其他常见元素
                    self.driver.find_element(By.TAG_NAME, "body")
                    print("详情页基本元素已加载")
                    
                    # 尝试多种可能的选择器
                    selectors = [
                        ".series-detail", 
                        ".car-detail", 
                        "[class*='detail']", 
                        "[class*='series-']"
                    ]
                    
                    element_found = False
                    for selector in selectors:
                        try:
                            WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                            )
                            print(f"找到详情页元素，使用选择器: {selector}")
                            element_found = True
                            break
                        except Exception:
                            continue
                    
                    if not element_found:
                        print("未找到详情页元素，尝试查看页面源码")
                        # 尝试截图保存
                        try:
                            screenshot_path = f"d:\\TRAE\\爬虫\\detail_screenshot_{url.split('/')[-1]}.png"
                            self.driver.save_screenshot(screenshot_path)
                            print(f"详情页截图已保存至: {screenshot_path}")
                        except Exception as ss_e:
                            print(f"截图失败: {ss_e}")
                except Exception as e:
                    print(f"详情页基本元素加载失败: {e}")
                
                return True
            except Exception as e:
                retry_count += 1
                print(f"获取详情页失败 (尝试 {retry_count}/{max_retries}): {e}")
                time.sleep(3)  # 等待一段时间后重试
        
        print(f"获取详情页失败，已达到最大重试次数 {max_retries}")
        return False
    
    def parse_car_detail(self, url):
        """解析汽车详情页，提取车辆详细信息"""
        try:
            # 根据实际页面结构调整选择器
            car_info = {
                'url': url,
                'name': self._safe_extract(".series-name"),
                'price': self._safe_extract(".series-price"),
                'brand': self._safe_extract(".brand-name"),
                'level': self._safe_extract(".car-level"),
                'score': self._safe_extract(".score-number"),
            }
            
            # 获取参数配置信息
            try:
                # 点击参数配置标签，如果有的话
                config_tabs = self.driver.find_elements(By.XPATH, "//div[contains(text(), '参数配置')]")
                if config_tabs:
                    config_tabs[0].click()
                    time.sleep(2)  # 增加等待时间
                    
                    # 获取发动机信息
                    car_info['engine'] = self._safe_extract(".engine-info, [class*='engine']")
                    # 获取变速箱信息
                    car_info['transmission'] = self._safe_extract(".transmission-info, [class*='transmission']")
                    # 获取车身结构
                    car_info['body_structure'] = self._safe_extract(".body-structure, [class*='body']")
            except Exception as e:
                print(f"获取参数配置失败: {e}")
            
            # 打印调试信息
            print(f"解析到车型信息: {car_info}")
            return car_info
        except Exception as e:
            print(f"解析车辆详情失败: {e}")
            return None
    
    def _safe_extract(self, selector):
        """安全提取元素文本"""
        try:
            # 支持多个选择器，用逗号分隔
            selectors = selector.split(',')
            for sel in selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, sel.strip())
                    if elements:
                        return elements[0].text.strip()
                except Exception:
                    continue
            return ""
        except Exception as e:
            print(f"提取元素 {selector} 失败: {e}")
            return ""
    
    def crawl(self, max_pages=1):
        """爬取指定页数的汽车信息"""
        for page in range(1, max_pages + 1):
            print(f"正在爬取第 {page} 页...")
            if not self.get_car_list_page(page):
                continue
            
            car_links = self.parse_car_list()
            print(f"第 {page} 页找到 {len(car_links)} 个车型链接")
            
            # 限制爬取的车型数量，避免时间过长
            max_cars = min(len(car_links), 10)
            for i, link in enumerate(car_links[:max_cars]):
                print(f"正在爬取第 {i+1}/{max_cars} 个车型: {link}")
                if self.get_car_detail(link):
                    car_info = self.parse_car_detail(link)
                    if car_info:
                        self.car_data.append(car_info)
                
                # 添加随机延迟，避免请求过于频繁
                delay = random.uniform(2, 5)
                print(f"等待 {delay:.2f} 秒...")
                time.sleep(delay)
            
            # 页面间延迟
            if page < max_pages:
                delay = random.uniform(3, 7)
                print(f"翻页前等待 {delay:.2f} 秒...")
                time.sleep(delay)
    
    def save_to_csv(self, filename="d:\\TRAE\\爬虫\\dongchedi_cars.csv"):
        """将爬取的数据保存为CSV文件"""
        if not self.car_data:
            print("没有数据可保存")
            return
        
        df = pd.DataFrame(self.car_data)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"数据已保存至 {filename}")
    
    def save_to_json(self, filename="d:\\TRAE\\爬虫\\dongchedi_cars.json"):
        """将爬取的数据保存为JSON文件"""
        if not self.car_data:
            print("没有数据可保存")
            return
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.car_data, f, ensure_ascii=False, indent=4)
        print(f"数据已保存至 {filename}")
    
    def close(self):
        """关闭WebDriver"""
        if hasattr(self, 'driver'):
            self.driver.quit()

if __name__ == "__main__":
    # 指定本地EdgeDriver路径，请替换为你的实际路径
    edgedriver_path = "d:\\TRAE\\爬虫\\msedgedriver.exe"  # 根据实际路径修改
    
    crawler = DongchediSeleniumCrawler(edgedriver_path)
    try:
        crawler.crawl(max_pages=1)  # 先只爬取1页进行测试
        crawler.save_to_csv()
        crawler.save_to_json()
    except Exception as e:
        print(f"爬取过程中发生错误: {e}")
    finally:
        crawler.close()