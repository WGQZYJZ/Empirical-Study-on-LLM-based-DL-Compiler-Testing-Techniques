'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data is: ', input_data)
result = torch.ceil(input_data)
print('Result is: ', result)