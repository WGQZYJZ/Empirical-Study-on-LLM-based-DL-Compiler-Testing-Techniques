'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input data: ', input_data)
result = torch.frac(input_data)
print('result: ', result)