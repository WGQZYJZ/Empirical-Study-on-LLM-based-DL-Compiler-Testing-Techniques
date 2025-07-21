'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arange\ntorch.arange(start=0, end, step=1, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
x = torch.arange(18).view(3, 2, 3)
print('Original tensor:', x)
print('Original tensor shape:', x.shape)
y = torch.arange(27).view(3, 3, 3)
print('Original tensor:', y)
print('Original tensor shape:', y.shape)