'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
import torch
input_data = torch.randn(10)
output_data = torch.clamp(input_data, min=(- 0.5), max=0.5)
print(input_data)
print(output_data)
print('Input: ', input_data)
print('Output: ', output_data)