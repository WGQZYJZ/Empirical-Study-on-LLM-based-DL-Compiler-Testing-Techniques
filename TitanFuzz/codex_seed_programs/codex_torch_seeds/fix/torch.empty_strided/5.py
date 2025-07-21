'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
x = torch.randn(3, 3)
print(x)
y = torch.empty_strided(size=(3, 3), stride=(1, 1))
print(y)
z = torch.empty_strided(size=(3, 3), stride=(2, 2))
print(z)