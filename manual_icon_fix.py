#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fix_china_ai_icons():
    """手动修复china-ai.html中的图标"""
    with open('china-ai.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 直接替换所有Google favicon服务为直接路径
    replacements = [
        ('https://www.google.com/s2/favicons?domain=qianwen.aliyun.com&sz=32', 'https://qianwen.aliyun.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=chatglm.cn&sz=32', 'https://chatglm.cn/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=xinghuo.xfyun.cn&sz=32', 'https://xinghuo.xfyun.cn/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=www.doubao.com&sz=32', 'https://www.doubao.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=kimi.moonshot.cn&sz=32', 'https://kimi.moonshot.cn/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=yige.baidu.com&sz=32', 'https://yige.baidu.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=wanxiang.aliyun.com&sz=32', 'https://wanxiang.aliyun.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=6pen.art&sz=32', 'https://6pen.art/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=aiart.chuangkit.com&sz=32', 'https://aiart.chuangkit.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=js.design&sz=32', 'https://js.design/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=ai.gaoding.com&sz=32', 'https://ai.gaoding.com/favicon.ico')
    ]
    
    for old_url, new_url in replacements:
        content = content.replace(old_url, new_url)
    
    # 替换简单的onerror为完整的fallback链
    content = content.replace(
        'onerror="this.style.display=\'none\'"',
        'onerror="this.onerror=null;this.src=this.src.replace(\'/favicon.ico\',\'/logo.png\');this.onerror=function(){this.onerror=null;this.src=this.src.replace(\'/logo.png\',\'/logo.jpg\');this.onerror=function(){this.onerror=null;this.src=this.src.replace(\'/logo.jpg\',\'/favicon.png\');this.onerror=function(){this.style.display=\'none\';}};}}"'
    )
    
    with open('china-ai.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("已修复china-ai.html中的图标")

def fix_img_icons():
    """手动修复img.html中的图标"""
    with open('img.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 直接替换所有Google favicon服务为直接路径
    replacements = [
        ('https://www.google.com/s2/favicons?domain=midjourney.com&sz=32', 'https://www.midjourney.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=remove.bg&sz=32', 'https://www.remove.bg/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=leonardo.ai&sz=32', 'https://leonardo.ai/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=bing.com&sz=32', 'https://www.bing.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=canva.com&sz=32', 'https://www.canva.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=photoroom.com&sz=32', 'https://www.photoroom.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=cutout.pro&sz=32', 'https://www.cutout.pro/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=letsenhance.io&sz=32', 'https://www.letsenhance.io/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=upscale.media&sz=32', 'https://www.upscale.media/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=tinypng.com&sz=32', 'https://tinypng.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=imagecompressor.com&sz=32', 'https://imagecompressor.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=picdiet.com&sz=32', 'https://www.picdiet.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=unsplash.com&sz=32', 'https://unsplash.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=pixabay.com&sz=32', 'https://pixabay.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=pexels.com&sz=32', 'https://www.pexels.com/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=promeai.pro&sz=32', 'https://www.promeai.pro/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=deepart.io&sz=32', 'https://deepart.io/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=krea.ai&sz=32', 'https://www.krea.ai/favicon.ico'),
        ('https://www.google.com/s2/favicons?domain=playground.bfl.ai&sz=32', 'https://playground.bfl.ai/favicon.ico')
    ]
    
    for old_url, new_url in replacements:
        content = content.replace(old_url, new_url)
    
    # 替换简单的onerror为完整的fallback链
    content = content.replace(
        'onerror="this.style.display=\'none\'"',
        'onerror="this.onerror=null;this.src=this.src.replace(\'/favicon.ico\',\'/logo.png\');this.onerror=function(){this.onerror=null;this.src=this.src.replace(\'/logo.png\',\'/logo.jpg\');this.onerror=function(){this.onerror=null;this.src=this.src.replace(\'/logo.jpg\',\'/favicon.png\');this.onerror=function(){this.style.display=\'none\';}};}}"'
    )
    
    with open('img.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("已修复img.html中的图标")

if __name__ == "__main__":
    fix_china_ai_icons()
    fix_img_icons()
    print("所有图标修复完成！") 