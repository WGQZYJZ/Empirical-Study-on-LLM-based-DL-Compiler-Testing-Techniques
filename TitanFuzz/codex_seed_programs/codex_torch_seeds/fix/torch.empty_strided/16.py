'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('input_data: ', input_data)
strided_data = torch.empty_strided(size=[1, 2, 3], stride=[3, 1, 1])
print('strided_data: ', strided_data)