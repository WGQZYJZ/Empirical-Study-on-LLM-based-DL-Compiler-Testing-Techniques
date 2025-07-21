'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = torch.ones(2, 3, 4)
print(input_data)
output_data = torch.empty_strided(input_data.shape, input_data.stride())
print(output_data)