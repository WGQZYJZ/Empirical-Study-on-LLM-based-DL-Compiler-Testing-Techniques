'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.arange(0, 3, 1)
y = torch.arange(0, 3, 1)
(x, y) = torch.meshgrid(x, y)
print(x)
print(y)
'\nTask 4: Call the API torch.stack\ntorch.stack(tensors, dim=0, out=None) → Tensor\n'
x = torch.arange(0, 3, 1)
y = torch.arange(0, 3, 1)
(x, y) = torch.meshgrid(x, y)
xy = torch.stack((x, y), dim=2)
print(xy)
'\nTask 5: Generate a random tensor\ntorch.rand(size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) → Tensor\n'
random_tensor = torch.rand(3, 3)
print(random_tensor)