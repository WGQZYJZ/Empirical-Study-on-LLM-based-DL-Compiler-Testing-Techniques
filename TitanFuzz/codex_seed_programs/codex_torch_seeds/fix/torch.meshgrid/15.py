'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.arange(0, 9, 1)
y = torch.arange(0, 5, 1)
(xx, yy) = torch.meshgrid(x, y)
print(xx)
print(yy)
import torch
x = torch.arange(0, 9, 1)
y = torch.arange(0, 5, 1)
(xx, yy) = torch.meshgrid(x, y)
print(xx)
print(yy)
import torch
x = torch.arange(0, 9, 1)
y = torch.arange(0, 5, 1)