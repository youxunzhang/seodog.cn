#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def add_icons_to_img_html():
    """为img.html中的工具卡片添加图标"""
    
    with open('img.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义工具和对应的图标映射
    tool_icons = {
        'Midjourney': 'https://www.midjourney.com/favicon.ico',
        'Remove.bg': 'https://www.remove.bg/favicon.ico',
        'Leonardo AI': 'https://leonardo.ai/favicon.ico',
        'Bing Image Creator': 'https://www.bing.com/favicon.ico',
        'Canva': 'https://www.canva.com/favicon.ico',
        'PhotoRoom': 'https://www.photoroom.com/favicon.ico',
        'Cutout.pro': 'https://www.cutout.pro/favicon.ico',
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
        # 构建新的图标HTML
        icon_html = f'<img src="{icon_url}" alt="{tool_name}" class="w-6 h-6 rounded mr-2" onerror="this.onerror=null;this.src=\'{icon_url.replace("/favicon.ico", "/logo.png")}\';this.onerror=function(){{this.onerror=null;this.src=\'{icon_url.replace("/favicon.ico", "/logo.jpg")}\';this.onerror=function(){{this.onerror=null;this.src=\'{icon_url.replace("/favicon.ico", "/favicon.png")}\';this.onerror=function(){{this.style.display=\'none\';}};}};}}">'
        
        # 查找工具标题并添加图标
        pattern = rf'<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">{re.escape(tool_name)}</h3>'
        replacement = f'<div class="flex items-center"><div class="flex items-center space-x-2">{icon_html}<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">{tool_name}</h3></div></div>'
        
        content = re.sub(pattern, replacement, content)
    
    # 写回文件
    with open('img.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("已为img.html中的工具卡片添加图标")

if __name__ == "__main__":
    add_icons_to_img_html() 