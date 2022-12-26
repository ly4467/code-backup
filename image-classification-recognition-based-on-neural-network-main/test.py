import torch
from PIL import Image
import torchvision

image_path = "./test_images/plane.png"
image = Image.open(image_path)
image = image.convert('RGB')

transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((32, 32)),
    torchvision.transforms.ToTensor()
])

image = transform(image)
print(image.shape)

model = torch.load("nnp_29.pth", map_location = torch.device("cpu"))
print(model)

image = torch.reshape(image, (1, 3, 32, 32))
model.eval()
with torch.no_grad():
    output = model(image)
print(output)
print(output.argmax(1))