from PIL import Image
import os

# 入力画像のパス
source_image_path = "C:/Users/michi/.gemini/antigravity/brain/9f9e9123-df68-4d3e-9dd6-6443a9d56b24/uploaded_image_1768708328778.png"

# プロジェクトのルートディレクトリ
project_root = "c:/Users/michi/OneDrive/デスクトップ/Vibe Coding/code/2026.1.18_SMA3rd_lp"
output_ico_path = os.path.join(project_root, "favicon.ico")
output_png_path = os.path.join(project_root, "favicon.png")

def create_favicon(source_path, output_ico, output_png):
    try:
        img = Image.open(source_path)
        
        # アルファチャンネルがあるか確認し、なければ追加（念のため）
        img = img.convert("RGBA")
        
        # 正方形にクロップする
        width, height = img.size
        new_size = min(width, height)
        
        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2
        
        # 中央でクロップ
        img_cropped = img.crop((left, top, right, bottom))
        
        # PNGとして保存 (透過維持、高解像度用)
        # 192x192程度にしておくとAndroidなどでも綺麗
        img_png = img_cropped.resize((192, 192), Image.LANCZOS)
        img_png.save(output_png, format="PNG")
        print(f"Created {output_png}")
        
        # ICOとして保存 (複数のサイズを含める)
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
        img_cropped.save(output_ico, format="ICO", sizes=icon_sizes)
        print(f"Created {output_ico}")
        
    except Exception as e:
        print(f"Error creating favicon: {e}")

if __name__ == "__main__":
    create_favicon(source_image_path, output_ico_path, output_png_path)
