import os
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image


def get_image_tensor(image_path):
    # 加载图片并进行预处理
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(Image.open(image_path))
    return image.unsqueeze(0)


def compare_images(image1_path, image2_path):
    # 加载模型
    model = models.resnet18(pretrained=True)
    model.eval()

    # 获取图片的特征向量
    image1_tensor = get_image_tensor(image1_path)
    image2_tensor = get_image_tensor(image2_path)
    with torch.no_grad():
        image1_features = model(image1_tensor)
        image2_features = model(image2_tensor)

    # 计算余弦相似度
    similarity = torch.nn.functional.cosine_similarity(image1_features, image2_features, dim=1)

    # 返回相似度结果
    return similarity.item()


def find_similar_images(folder_path, threshold):
    # 获取文件夹中所有图片的路径
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".jpg")]

    # 比较所有图片的相似度
    for i in range(len(image_paths)):
        for j in range(i+1, len(image_paths)):
            image1_path = image_paths[i]
            image2_path = image_paths[j]
            similarity = compare_images(image1_path, image2_path)

            # 如果相似度超过阈值，则输出结果
            if similarity > threshold:
                print(f"Similar images: {image1_path} and {image2_path}")
                print(f"Similarity: {similarity}")


folder_path = "D:/Users/User/Desktop/wallpaper"  # 文件夹路径
os.chdir(folder_path)
# 查找文件夹中相似的图片
find_similar_images(".", 0.9)
