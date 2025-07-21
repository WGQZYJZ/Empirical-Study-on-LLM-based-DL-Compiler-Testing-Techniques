'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.randn(3, 4)
print('Input data: ', input_data)
result = torch.amin(input_data, dim=1)
print('Result: ', result)