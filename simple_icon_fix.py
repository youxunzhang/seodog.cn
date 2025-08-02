#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fix_icons():
    """修复图标问题"""
    
    # 修复china-ai.html
    try:
        with open('china-ai.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换通义千问的图标
        content = content.replace(
            'https://www.google.com/s2/favicons?domain=qianwen.aliyun.com&sz=32',
            'https://qianwen.aliyun.com/favicon.ico'
        )
        content = content.replace(
            'onerror="this.style.display=\'none\'"',
            'onerror="this.onerror=null;this.src=\'https://qianwen.aliyun.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://qianwen.aliyun.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://qianwen.aliyun.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}}"'
        )
        
        # 替换其他网站的图标
        replacements = [
            ('chatglm.cn', 'https://chatglm.cn/favicon.ico'),
            ('xinghuo.xfyun.cn', 'https://xinghuo.xfyun.cn/favicon.ico'),
            ('www.doubao.com', 'https://www.doubao.com/favicon.ico'),
            ('kimi.moonshot.cn', 'https://kimi.moonshot.cn/favicon.ico'),
            ('yige.baidu.com', 'https://yige.baidu.com/favicon.ico'),
            ('wanxiang.aliyun.com', 'https://wanxiang.aliyun.com/favicon.ico'),
            ('6pen.art', 'https://6pen.art/favicon.ico'),
            ('aiart.chuangkit.com', 'https://aiart.chuangkit.com/favicon.ico'),
            ('js.design', 'https://js.design/favicon.ico'),
            ('ai.gaoding.com', 'https://ai.gaoding.com/favicon.ico')
        ]
        
        for domain, favicon in replacements:
            content = content.replace(
                f'https://www.google.com/s2/favicons?domain={domain}&sz=32',
                favicon
            )
        
        with open('china-ai.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("已修复china-ai.html中的图标")
        
    except Exception as e:
        print(f"修复china-ai.html时出错: {e}")
    
    # 修复img.html
    try:
        with open('img.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换img.html中的图标
        img_replacements = [
            ('midjourney.com', 'https://www.midjourney.com/favicon.ico'),
            ('remove.bg', 'https://www.remove.bg/favicon.ico'),
            ('leonardo.ai', 'https://leonardo.ai/favicon.ico'),
            ('bing.com', 'https://www.bing.com/favicon.ico'),
            ('canva.com', 'https://www.canva.com/favicon.ico'),
            ('photoroom.com', 'https://www.photoroom.com/favicon.ico'),
            ('cutout.pro', 'https://www.cutout.pro/favicon.ico'),
            ('letsenhance.io', 'https://www.letsenhance.io/favicon.ico'),
            ('upscale.media', 'https://www.upscale.media/favicon.ico'),
            ('tinypng.com', 'https://tinypng.com/favicon.ico'),
            ('imagecompressor.com', 'https://imagecompressor.com/favicon.ico'),
            ('picdiet.com', 'https://www.picdiet.com/favicon.ico'),
            ('unsplash.com', 'https://unsplash.com/favicon.ico'),
            ('pixabay.com', 'https://pixabay.com/favicon.ico'),
            ('pexels.com', 'https://www.pexels.com/favicon.ico'),
            ('promeai.pro', 'https://www.promeai.pro/favicon.ico'),
            ('deepart.io', 'https://deepart.io/favicon.ico'),
            ('krea.ai', 'https://www.krea.ai/favicon.ico'),
            ('playground.bfl.ai', 'https://playground.bfl.ai/favicon.ico')
        ]
        
        for domain, favicon in img_replacements:
            content = content.replace(
                f'https://www.google.com/s2/favicons?domain={domain}&sz=32',
                favicon
            )
        
        with open('img.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("已修复img.html中的图标")
        
    except Exception as e:
        print(f"修复img.html时出错: {e}")

if __name__ == "__main__":
    fix_icons() 