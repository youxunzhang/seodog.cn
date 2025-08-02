#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def update_china_ai_favicons():
    """更新china-ai.html中的剩余favicon图标"""
    
    with open('china-ai.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义需要更新的图标映射
    replacements = [
        # 通义千问
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=qianwen\.aliyun\.com&sz=32" alt="通义千问" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://qianwen.aliyun.com/favicon.ico" alt="通义千问" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://qianwen.aliyun.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://qianwen.aliyun.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://qianwen.aliyun.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 智谱AI
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=chatglm\.cn&sz=32" alt="智谱AI" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://chatglm.cn/favicon.ico" alt="智谱AI" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://chatglm.cn/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://chatglm.cn/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://chatglm.cn/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 讯飞星火
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=xinghuo\.xfyun\.cn&sz=32" alt="讯飞星火" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://xinghuo.xfyun.cn/favicon.ico" alt="讯飞星火" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://xinghuo.xfyun.cn/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://xinghuo.xfyun.cn/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://xinghuo.xfyun.cn/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 豆包
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=www\.doubao\.com&sz=32" alt="豆包" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://www.doubao.com/favicon.ico" alt="豆包" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://www.doubao.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://www.doubao.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://www.doubao.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 月之暗面
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=kimi\.moonshot\.cn&sz=32" alt="月之暗面" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://kimi.moonshot.cn/favicon.ico" alt="月之暗面" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://kimi.moonshot.cn/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://kimi.moonshot.cn/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://kimi.moonshot.cn/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 文心一格
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=yige\.baidu\.com&sz=32" alt="文心一格" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://yige.baidu.com/favicon.ico" alt="文心一格" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://yige.baidu.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://yige.baidu.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://yige.baidu.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 通义万相
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=wanxiang\.aliyun\.com&sz=32" alt="通义万相" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://wanxiang.aliyun.com/favicon.ico" alt="通义万相" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://wanxiang.aliyun.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://wanxiang.aliyun.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://wanxiang.aliyun.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 6pen Art
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=6pen\.art&sz=32" alt="6pen Art" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://6pen.art/favicon.ico" alt="6pen Art" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://6pen.art/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://6pen.art/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://6pen.art/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 爱作画
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=aiart\.chuangkit\.com&sz=32" alt="爱作画" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://aiart.chuangkit.com/favicon.ico" alt="爱作画" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://aiart.chuangkit.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://aiart.chuangkit.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://aiart.chuangkit.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 即时设计
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=js\.design&sz=32" alt="即时设计" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://js.design/favicon.ico" alt="即时设计" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://js.design/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://js.design/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://js.design/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        ),
        # 稿定AI
        (
            r'<img src="https://www\.google\.com/s2/favicons\?domain=ai\.gaoding\.com&sz=32" alt="稿定AI" class="w-6 h-6 rounded" onerror="this\.style\.display=\'none\'">',
            '<img src="https://ai.gaoding.com/favicon.ico" alt="稿定AI" class="w-6 h-6 rounded" onerror="this.onerror=null;this.src=\'https://ai.gaoding.com/logo.png\';this.onerror=function(){this.onerror=null;this.src=\'https://ai.gaoding.com/logo.jpg\';this.onerror=function(){this.onerror=null;this.src=\'https://ai.gaoding.com/favicon.png\';this.onerror=function(){this.style.display=\'none\';}};}">'
        )
    ]
    
    # 执行替换
    for old_pattern, new_replacement in replacements:
        content = re.sub(old_pattern, new_replacement, content)
    
    # 写回文件
    with open('china-ai.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("已更新china-ai.html中的favicon图标")

if __name__ == "__main__":
    update_china_ai_favicons() 