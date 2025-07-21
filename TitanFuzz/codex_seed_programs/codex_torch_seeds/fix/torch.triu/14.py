'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data: \n', input_data)
output = torch.triu(input_data)
print('Output: \n', output)
output = torch.triu(input_data, diagonal=1)
print('Output: \n', output)