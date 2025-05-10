import cv2
import os

# 定义图片文件夹路径
input_folder = "../photo/photo"
left_folder = "../photo/left"
right_folder = "../photo/right"

# 创建输出文件夹（如果不存在）
os.makedirs(left_folder, exist_ok=True)
os.makedirs(right_folder, exist_ok=True)

# 遍历文件夹中的图片文
for i in range(1, 80):  # 假设图片文件名为 photo(1), photo(2), ..., photo(99)
    file_name = f"photo ({i}).bmp"
    file_path = os.path.join(input_folder, file_name)

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"文件 {file_name} 不存在，跳过...")
        continue

    # 读取图片
    image = cv2.imread(file_path)

    # 获取图片的高度和宽度
    height, width, _ = image.shape

    # 确保宽度可以被2整除
    if width % 2 != 0:
        print(f"图片 {file_name} 宽度不是偶数，无法均分裁剪")
        continue

    # 计算左右图片的宽度
    half_width = width // 2

    # 裁剪左半部分
    left_image = image[:, :half_width]

    # 裁剪右半部分
    right_image = image[:, half_width:]

    # 保存裁剪后的图片
    left_image_path = os.path.join(left_folder, f"img{i}.jpg")
    right_image_path = os.path.join(right_folder, f"img{i}.jpg")
    cv2.imwrite(left_image_path, left_image)
    cv2.imwrite(right_image_path, right_image)

    print(f"图片 {file_name} 裁剪完成，已保存为 {left_image_path} 和 {right_image_path}")