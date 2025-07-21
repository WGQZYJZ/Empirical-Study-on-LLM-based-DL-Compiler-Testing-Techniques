'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atleast_3d\ntorch.atleast_3d(*tensors)\n'
import torch
x = torch.rand(2, 3, 4)
y = torch.rand(4, 2)
z = torch.atleast_3d(x, y)
print(z)