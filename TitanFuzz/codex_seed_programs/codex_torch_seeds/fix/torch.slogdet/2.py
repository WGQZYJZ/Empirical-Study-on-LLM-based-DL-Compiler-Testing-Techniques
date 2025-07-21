'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
input = torch.randn(1, 2, 3, 3)
print('Input data: ', input)
print('Output: ', torch.slogdet(input))