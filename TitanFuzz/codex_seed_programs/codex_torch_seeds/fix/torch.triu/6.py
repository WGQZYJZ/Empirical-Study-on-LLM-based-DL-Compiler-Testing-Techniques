'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data:')
print(input_data)
print('\nOutput data:')
print(torch.triu(input_data))
print('\nOutput data:')
print(torch.triu(input_data, diagonal=1))
print('\nOutput data:')
print(torch.triu(input_data, diagonal=(- 1)))