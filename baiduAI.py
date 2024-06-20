import paddle  
import paddle.vision.transforms as T  
from paddle.vision.datasets import ImageFolder  
  
# 定义预处理函数  
transform = T.Compose([  
    T.Resize((224, 224)),  
    T.ToTensor(),  
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  
])  
  
# 加载数据集  
train_dataset = ImageFolder('path/to/train/folder', transform=transform)  
test_dataset = ImageFolder('path/to/test/folder', transform=transform)  
  
# 创建模型  
model = paddle.vision.models.resnet18(pretrained=True)  
  
# 定义损失函数和优化器  
criterion = paddle.nn.CrossEntropyLoss()  
optimizer = paddle.optimizer.Adam(learning_rate=0.001)  
  
# 定义API调用函数  
def ask_question():  
    # 获取问题文本  
    question = input('请输入问题：')  
  
    # 调用文心一言API提问问题  
    result = paddle.vision.transforms.ToTensor().unsqueeze(0).eval()  
    result = paddle.vision.models.resnet18().predict(result)  
    result = paddle.argmax(result, axis=1).numpy()  
    result = result[0, 0]  
    result = result.astype('int32')  
    result = paddle.to_tensor(result, dtype='float32')  
    result = paddle.vision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(result)  
    result = paddle.to_tensor([question], dtype='float32').unsqueeze(0)