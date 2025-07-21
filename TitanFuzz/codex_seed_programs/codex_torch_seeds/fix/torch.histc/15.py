'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(1000)
print('Task 3: Call the API torch.histc')
result = torch.histc(input_data, bins=100, min=0, max=0)
print('result: ', result)