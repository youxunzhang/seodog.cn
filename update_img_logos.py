#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新img.html文件中的工具LOGO
"""

import re

def update_tool_logos():
    # 读取文件
    with open('img.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义工具和对应的域名
    tools = [
        ('Leonardo AI', 'leonardo.ai'),
        ('Bing Create', 'bing.com'),
        ('Canva AI', 'canva.com'),
        ('PhotoRoom', 'photoroom.com'),
        ('Cutout Pro', 'cutout.pro'),
        ('Let\'s Enhance', 'letsenhance.io'),
        ('GFPGAN', 'huggingface.co'),
        ('Upscale Media', 'upscale.media'),
        ('TinyPNG', 'tinypng.com'),
        ('Image Compressor', 'imagecompressor.com'),
        ('PicDiet', 'picdiet.com'),
        ('Unsplash', 'unsplash.com'),
        ('Pixabay', 'pixabay.com'),
        ('Pexels', 'pexels.com'),
        ('PromeAI', 'promeai.pro'),
        ('DeepArt', 'deepart.io'),
        ('Krea AI', 'krea.ai'),
        ('BFL AI Playground', 'bfl.ai')
    ]
    
    # 为每个工具添加LOGO
    for tool_name, domain in tools:
        # 查找工具标题行
        pattern = rf'<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">{re.escape(tool_name)}</h3>'
        replacement = f'''<div class="flex items-center space-x-2">
              <img src="https://www.google.com/s2/favicons?domain={domain}&sz=32" alt="{tool_name}" class="w-6 h-6 rounded" onerror="this.style.display='none'">
              <h3 class="text-lg lg:text-xl font-bold text-responsive-lg">{tool_name}</h3>
            </div>'''
        
        content = re.sub(pattern, replacement, content)
    
    # 写回文件
    with open('img.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 已成功更新所有工具LOGO！")

if __name__ == "__main__":
    update_tool_logos() 