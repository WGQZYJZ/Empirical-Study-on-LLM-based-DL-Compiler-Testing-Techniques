'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
y = torch.nn.Softmax(dim=0)(x)
print(y)