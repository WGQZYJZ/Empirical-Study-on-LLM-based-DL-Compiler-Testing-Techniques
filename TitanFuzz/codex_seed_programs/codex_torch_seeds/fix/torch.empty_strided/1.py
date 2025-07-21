'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
size = (2, 3, 4)
stride = (8, 4, 2)
output = torch.empty_strided(size, stride)
print('Output tensor: ', output)