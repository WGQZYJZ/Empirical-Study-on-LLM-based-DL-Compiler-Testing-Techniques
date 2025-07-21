'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.median\ntorch.median(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 3, 4)
print('Input data: ', input_data)
median_output = torch.median(input_data, dim=1, keepdim=False)
print('Median output: ', median_output)