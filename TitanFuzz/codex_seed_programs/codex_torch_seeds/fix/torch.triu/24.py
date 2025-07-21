'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: ', input)
triu_input = torch.triu(input)
print('Triu Input: ', triu_input)
triu_input = torch.triu(input, diagonal=1)
print('Triu Input: ', triu_input)
triu_input = torch.triu(input, diagonal=(- 1))
print('Triu Input: ', triu_input)
triu_input = torch.triu(input, diagonal=0)
print('Triu Input: ', triu_input)