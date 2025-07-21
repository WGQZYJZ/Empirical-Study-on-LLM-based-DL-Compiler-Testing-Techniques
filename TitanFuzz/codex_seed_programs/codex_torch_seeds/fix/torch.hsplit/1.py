'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
data = torch.arange(0, 24).reshape(4, 6)
print('Input data:')
print(data)
print('\nSplit the input data into two parts:')
result = torch.hsplit(data, 2)
print(result)
print('\nSplit the input data into three parts:')
result = torch.hsplit(data, 3)
print(result)