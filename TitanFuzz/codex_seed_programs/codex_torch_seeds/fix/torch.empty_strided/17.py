'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = torch.rand(2, 3, 4, 5)
output_data = torch.empty_strided(input_data.size(), input_data.stride())
print('input_data: ', input_data)
print('output_data: ', output_data)