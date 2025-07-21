'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.arange(0, 3)
y = torch.arange(0, 3)
print(x)
print(y)
(xx, yy) = torch.meshgrid(x, y)
print(xx)
print(yy)