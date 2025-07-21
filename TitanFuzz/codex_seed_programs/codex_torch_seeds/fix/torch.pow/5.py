'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('input data: ', input_data)
result = torch.pow(input_data, 3)
print('result: ', result)