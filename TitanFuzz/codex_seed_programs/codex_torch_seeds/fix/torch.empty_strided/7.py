'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
size = [2, 2]
stride = [1, 2]
x = torch.empty_strided(size, stride)
print('x = ', x)
print('x.size() = ', x.size())
print('x.stride() = ', x.stride())