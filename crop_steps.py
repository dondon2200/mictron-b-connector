from PIL import Image

img = Image.open("/home/ubuntu/b_connector/images/reference/how_to_use.png")
w, h = img.size
print(f"Original size: {w} x {h}")

# 圖片是 4 步驟橫向排列，每步驟寬度約 w/4
step_w = w // 4

for i in range(4):
    left = i * step_w
    right = left + step_w
    cropped = img.crop((left, 0, right, h))
    cropped.save(f"/home/ubuntu/b_connector/images/step_{i+1}.png")
    print(f"Saved step_{i+1}.png: {left},{0} -> {right},{h}")
