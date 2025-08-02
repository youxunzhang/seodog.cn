#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有页面的图标问题
确保准确获取网站LOGO
"""

import re
import os

def fix_china_ai_icons():
    """修复china-ai.html中的图标"""
    with open('china-ai.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义网站图标映射
    icon_mappings = {
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
        'ai.gaoding.com': 'https://ai.gaoding.com/favicon.ico'
    }
    
    # 替换Google favicon服务为直接路径
    for domain, favicon_url in icon_mappings.items():
        google_pattern = rf'https://www\.google\.com/s2/favicons\?domain={re.escape(domain)}&sz=32'
        new_onerror = f'''onerror="this.onerror=null;this.src='https://{domain}/logo.png';this.onerror=function(){{this.onerror=null;this.src='https://{domain}/logo.jpg';this.onerror=function(){{this.onerror=null;this.src='https://{domain}/favicon.png';this.onerror=function(){{this.style.display='none';}};}};}}"`
        
        # 替换模式
        old_pattern = rf'<img src="{google_pattern}"([^>]*?)onerror="[^"]*"([^>]*?)>'
        new_replacement = rf'<img src="{favicon_url}"\1{new_onerror}\2>'
        content = re.sub(old_pattern, new_replacement, content)
    
    with open('china-ai.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("已修复china-ai.html中的图标")

def fix_img_icons():
    """为img.html添加图标"""
    with open('img.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义工具图标映射
    tool_icons = {
        'Midjourney': 'https://www.midjourney.com/favicon.ico',
        'Remove.bg': 'https://www.remove.bg/favicon.ico',
        'Leonardo AI': 'https://leonardo.ai/favicon.ico',
        'Bing Create': 'https://www.bing.com/favicon.ico',
        'Canva AI': 'https://www.canva.com/favicon.ico',
        'PhotoRoom': 'https://www.photoroom.com/favicon.ico',
        'Cutout Pro': 'https://www.cutout.pro/favicon.ico',
        'Let\'s Enhance': 'https://www.letsenhance.io/favicon.ico',
        'Upscale Media': 'https://www.upscale.media/favicon.ico',
        'TinyPNG': 'https://tinypng.com/favicon.ico',
        'Image Compressor': 'https://imagecompressor.com/favicon.ico',
        'PicDiet': 'https://www.picdiet.com/favicon.ico',
        'Unsplash': 'https://unsplash.com/favicon.ico',
        'Pixabay': 'https://pixabay.com/favicon.ico',
        'Pexels': 'https://www.pexels.com/favicon.ico',
        'PromeAI': 'https://www.promeai.pro/favicon.ico',
        'DeepArt': 'https://deepart.io/favicon.ico',
        'Krea AI': 'https://www.krea.ai/favicon.ico',
        'BFL AI Playground': 'https://playground.bfl.ai/favicon.ico'
    }
    
    # 为每个工具添加图标
    for tool_name, icon_url in tool_icons.items():
        domain = icon_url.split('/favicon.ico')[0]
        icon_html = f'''<img src="{icon_url}" alt="{tool_name}" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src='{domain}/logo.png';this.onerror=function(){{this.onerror=null;this.src='{domain}/logo.jpg';this.onerror=function(){{this.onerror=null;this.src='{domain}/favicon.png';this.onerror=function(){{this.style.display='none';}};}};}}">'''
        
        # 查找并替换h3标签
        pattern = rf'<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">{re.escape(tool_name)}</h3>'
        replacement = f'<div class="flex items-center space-x-2">{icon_html}<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">{tool_name}</h3></div>'
        
        content = content.replace(pattern, replacement)
    
    with open('img.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("已为img.html添加图标")

def main():
    """主函数"""
    try:
        if os.path.exists('china-ai.html'):
            fix_china_ai_icons()
        else:
            print("china-ai.html 文件不存在")
        
        if os.path.exists('img.html'):
            fix_img_icons()
        else:
            print("img.html 文件不存在")
            
        print("图标修复完成！")
        
    except Exception as e:
        print(f"修复过程中出现错误: {e}")

if __name__ == "__main__":
    main() 