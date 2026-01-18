
import os
import re

file_path = r'c:\Users\michi\OneDrive\デスクトップ\Vibe Coding\code\2026.1.18_SMA3rd_lp\style.css'

# よりインパクトのあるデザインに変更
new_css = """
/* Hero Section Styles Update (Enhanced Visibility) */
.hero-subtitle {
    display: block;
    font-size: 1.2rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 1rem;
    text-transform: uppercase;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

.hero-term-highlight {
    display: inline-block;
    font-size: clamp(1.8rem, 4vw, 2.6rem); /* 最大2.6remまで大きく */
    font-weight: 800; /* より太く */
    color: #FFD700; /* 明るいゴールド */
    background: rgba(0, 0, 0, 0.5); /* 背景を暗くしてコントラスト確保 */
    padding: 0.8rem 2rem;
    border: 1px solid rgba(255, 215, 0, 0.5); /* ゴールドの枠線 */
    border-radius: 8px; /* 角丸 */
    margin-bottom: 2rem;
    letter-spacing: 0.1em;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.6), 0 0 10px rgba(0,0,0,0.8);
    backdrop-filter: blur(4px); /* 背景ぼかしでモダンに */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    animation: fadeInUp 0.8s ease-out forwards;
}

.hero-title {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 30px rgba(255, 255, 255, 0.2);
}

@media (max-width: 768px) {
    .hero-term-highlight {
        font-size: 1.6rem; /* スマホでも十分大きく */
        padding: 0.6rem 1.5rem;
        margin-bottom: 1.5rem;
        width: 90%; /* 幅を持たせて目立たせる */
    }
    .hero-title {
        font-size: 2.2rem;
    }
}
"""

try:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 既存の "Hero Section Styles Update" ブロックがあれば削除して入れ替える
    marker = "/* Hero Section Styles Update"
    marker_index = content.find(marker)
    
    if marker_index != -1:
        # マーカーが見つかったら、そこからファイル末尾まで（または次のセクションまで）を置換対象とする
        # 今回は末尾に追加しているはずなので、マーカー以降を切り捨てる
        clean_content = content[:marker_index]
    else:
        # 万が一マーカーがない場合は、末尾の閉じ括弧チェックを行う（前回のロジック）
        last_brace_index = content.rfind('}')
        if last_brace_index != -1 and last_brace_index > len(content) - 1000:
             clean_content = content[:last_brace_index+1]
        else:
             clean_content = content

    # Append new CSS
    final_content = clean_content.strip() + "\n\n" + new_css
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("Successfully updated style.css with enhanced visibility styles")

except Exception as e:
    print(f"Error: {e}")
