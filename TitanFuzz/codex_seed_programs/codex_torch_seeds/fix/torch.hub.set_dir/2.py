'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.set_dir\ntorch.hub.set_dir(d)\n'
import torch
x = torch.randn(1, 3, 224, 224, requires_grad=True)
torch.hub.set_dir('/tmp/hub_dir')
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
y = model(x)
probs = torch.nn.functional.softmax(y, dim=1)
(values, indices) = torch.topk(probs, 3)
print(values)
print(indices)