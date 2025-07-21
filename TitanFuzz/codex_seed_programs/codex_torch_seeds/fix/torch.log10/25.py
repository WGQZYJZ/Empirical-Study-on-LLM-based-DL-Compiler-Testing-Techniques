'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
input_data = torch.Tensor([2.0, 3.0, 4.0])
print('Input data: ', input_data)
print('Output data: ', torch.log10(input_data))