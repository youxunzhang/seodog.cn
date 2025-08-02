#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新HTML文件中的favicon图标
使用目标网站的实际logo地址替代Google favicon服务
"""

import re
import os

def update_favicon_urls(file_path):
    """更新HTML文件中的favicon图标URL"""
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义网站和对应的logo地址映射
    site_logos = {
        'yiyan.baidu.com': 'https://yiyan.baidu.com/favicon.ico',
        'qianwen.aliyun.com': 'https://qianwen.aliyun.com/favicon.ico',
        'chatglm.cn': 'https://chatglm.cn/favicon.ico',
        'xinghuo.xfyun.cn': 'https://xinghuo.xfyun.cn/favicon.ico',
        'www.doubao.com': 'https://www.doubao.com/favicon.ico',
        'kimi.moonshot.cn': 'https://kimi.moonshot.cn/favicon.ico',
        'yige.baidu.com': 'https://yige.baidu.com/favicon.ico',
        'wanxiang.aliyun.com': 'https://wanxiang.aliyun.com/favicon.ico',
        '6pen.art': 'https://6pen.art/favicon.ico',
        'aiart.chuangkit.com': 'https://aiart.chuangkit.com/favicon.ico',
        'js.design': 'https://js.design/favicon.ico',
        'ai.gaoding.com': 'https://ai.gaoding.com/favicon.ico',
        'www.midjourney.com': 'https://www.midjourney.com/favicon.ico',
        'www.remove.bg': 'https://www.remove.bg/favicon.ico',
        'leonardo.ai': 'https://leonardo.ai/favicon.ico',
        'www.bing.com': 'https://www.bing.com/favicon.ico',
        'www.canva.com': 'https://www.canva.com/favicon.ico',
        'www.photoroom.com': 'https://www.photoroom.com/favicon.ico',
        'www.cutout.pro': 'https://www.cutout.pro/favicon.ico',
        'www.letsenhance.io': 'https://www.letsenhance.io/favicon.ico',
        'www.upscale.media': 'https://www.upscale.media/favicon.ico',
        'tinypng.com': 'https://tinypng.com/favicon.ico',
        'imagecompressor.com': 'https://imagecompressor.com/favicon.ico',
        'www.picdiet.com': 'https://www.picdiet.com/favicon.ico',
        'unsplash.com': 'https://unsplash.com/favicon.ico',
        'pixabay.com': 'https://pixabay.com/favicon.ico',
        'www.pexels.com': 'https://www.pexels.com/favicon.ico',
        'www.promeai.pro': 'https://www.promeai.pro/favicon.ico',
        'deepart.io': 'https://deepart.io/favicon.ico',
        'www.krea.ai': 'https://www.krea.ai/favicon.ico',
        'playground.bfl.ai': 'https://playground.bfl.ai/favicon.ico'
    }
    
    # 新的onerror处理逻辑
    new_onerror = '''onerror="this.onerror=null;this.src='{domain}/logo.png';this.onerror=function(){{this.onerror=null;this.src='{domain}/logo.jpg';this.onerror=function(){{this.onerror=null;this.src='{domain}/favicon.png';this.onerror=function(){{this.style.display='none';}};}};}}"'''
    
    # 替换Google favicon服务URL
    for domain, favicon_url in site_logos.items():
        # 构建Google favicon服务的URL模式
        google_favicon_pattern = rf'https://www\.google\.com/s2/favicons\?domain={re.escape(domain)}&sz=32'
        
        # 构建新的img标签
        new_img_src = favicon_url
        new_onerror_attr = new_onerror.format(domain=f"https://{domain}")
        
        # 替换模式
        old_pattern = rf'<img src="{google_favicon_pattern}"([^>]*?)onerror="[^"]*"([^>]*?)>'
        new_replacement = rf'<img src="{new_img_src}"\1{new_onerror_attr}\2>'
        
        # 执行替换
        content = re.sub(old_pattern, new_replacement, content)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已更新文件: {file_path}")

def main():
    """主函数"""
    # 需要更新的HTML文件列表
    html_files = [
        'china-ai.html',
        'img.html',
        'index.html'
    ]
    
    for file_path in html_files:
        if os.path.exists(file_path):
            try:
                update_favicon_urls(file_path)
            except Exception as e:
                print(f"更新文件 {file_path} 时出错: {e}")
        else:
            print(f"文件不存在: {file_path}")

if __name__ == "__main__":
    main() 