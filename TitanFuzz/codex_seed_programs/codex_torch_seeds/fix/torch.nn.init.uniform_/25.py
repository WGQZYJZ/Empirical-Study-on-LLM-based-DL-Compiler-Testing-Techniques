'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
input = torch.empty(5, 7)
print('input: ', input)
torch.nn.init.uniform_(input)
print('input: ', input)
input = torch.empty(5, 7)
print('input: ', input)
torch.nn.init.uniform_(input, 5, 10)
print('input: ', input)
input = torch.empty(5, 7)
print('input: ', input)