#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_icons_to_img():
    """为img.html添加图标"""
    
    with open('img.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换Midjourney的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Midjourney</h3>',
        '<div class="flex items-center space-x-2"><img src="https://www.midjourney.com/favicon.ico" alt="Midjourney" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://www.midjourney.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://www.midjourney.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://www.midjourney.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Midjourney</h3></div>'
    )
    
    # 替换Remove.bg的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Remove.bg</h3>',
        '<div class="flex items-center space-x-2"><img src="https://www.remove.bg/favicon.ico" alt="Remove.bg" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://www.remove.bg/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://www.remove.bg/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://www.remove.bg/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Remove.bg</h3></div>'
    )
    
    # 替换Leonardo AI的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Leonardo AI</h3>',
        '<div class="flex items-center space-x-2"><img src="https://leonardo.ai/favicon.ico" alt="Leonardo AI" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://leonardo.ai/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://leonardo.ai/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://leonardo.ai/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Leonardo AI</h3></div>'
    )
    
    # 替换Bing Create的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Bing Create</h3>',
        '<div class="flex items-center space-x-2"><img src="https://www.bing.com/favicon.ico" alt="Bing Create" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://www.bing.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://www.bing.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://www.bing.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Bing Create</h3></div>'
    )
    
    # 替换Canva AI的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Canva AI</h3>',
        '<div class="flex items-center space-x-2"><img src="https://www.canva.com/favicon.ico" alt="Canva AI" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://www.canva.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://www.canva.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://www.canva.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Canva AI</h3></div>'
    )
    
    # 替换Krea AI的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Krea AI</h3>',
        '<div class="flex items-center space-x-2"><img src="https://www.krea.ai/favicon.ico" alt="Krea AI" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://www.krea.ai/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://www.krea.ai/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://www.krea.ai/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">Krea AI</h3></div>'
    )
    
    # 替换BFL AI Playground的标题
    content = content.replace(
        '<h3 class="text-lg lg:text-xl font-bold text-responsive-lg">BFL AI Playground</h3>',
        '<div class="flex items-center space-x-2"><img src="https://playground.bfl.ai/favicon.ico" alt="BFL AI Playground" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://playground.bfl.ai/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://playground.bfl.ai/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://playground.bfl.ai/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}"><h3 class="text-lg lg:text-xl font-bold text-responsive-lg">BFL AI Playground</h3></div>'
    )
    
    with open('img.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("已为img.html添加图标")

if __name__ == "__main__":
    add_icons_to_img() 