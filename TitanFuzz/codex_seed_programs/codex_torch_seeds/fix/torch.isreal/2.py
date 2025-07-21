'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
input = torch.randn(3, 3)
print('input: ', input)
output = torch.isreal(input)
print('output: ', output)