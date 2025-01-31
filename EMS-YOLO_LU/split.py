import os
import shutil

# 设置你的文件夹路径
txt_file_path = '/media/asus/299D817A2D97AD941/ok_PROJs/EMS-YOLO-main/data/SAR-AIRcraft-1.0/ImageSets/Main/test.txt'  # 指向包含图片名称的txt文件
annotations_dir = '/media/asus/299D817A2D97AD941/ok_PROJs/EMS-YOLO-main/data/SAR-AIRcraft-1.0/JPEGImages'  # 指向包含xml文件的annotations文件夹
val_dir = '/media/asus/299D817A2D97AD941/ok_PROJs/EMS-YOLO-main/data/SAR-AIRcraft-1.0/JPEGImages/test'  # 指向目标val文件夹

# 读取txt文件中的图片名称
with open(txt_file_path, 'r') as file:
    image_names = file.read().splitlines()  # 读取所有行并分割成列表

# 遍历图片名称列表
for image_name in image_names:
    # 构建源xml文件的路径
    source_xml_path = os.path.join(annotations_dir, f"{image_name}.jpg")
    
    # 检查源xml文件是否存在
    if os.path.exists(source_xml_path):
        # 构建目标xml文件的路径
        destination_xml_path = os.path.join(val_dir, f"{image_name}.jpg")
        
        # 复制文件
        shutil.copy(source_xml_path, destination_xml_path)
        print(f"Copied {source_xml_path} to {destination_xml_path}")
    else:
        print(f"File not found: {source_xml_path}")

print("Copy operation completed.")