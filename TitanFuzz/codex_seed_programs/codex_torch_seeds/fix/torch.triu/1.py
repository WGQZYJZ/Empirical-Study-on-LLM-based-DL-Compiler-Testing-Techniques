'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('input_data: ', input_data)
triu_data = torch.triu(input_data)
print('triu_data: ', triu_data)