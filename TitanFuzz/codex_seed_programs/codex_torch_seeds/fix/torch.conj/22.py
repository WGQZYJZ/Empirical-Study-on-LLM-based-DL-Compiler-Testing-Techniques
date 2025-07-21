'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj\ntorch.conj(input)\n'
import torch
input = torch.randn(3, 3)
print('Input data: ', input)
output = torch.conj(input)
print('Output data: ', output)