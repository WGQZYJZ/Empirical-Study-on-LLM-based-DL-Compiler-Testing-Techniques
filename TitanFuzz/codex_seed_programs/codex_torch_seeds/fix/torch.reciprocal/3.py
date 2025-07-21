'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
data = torch.randn(2, 2)
print('Input data:')
print(data)
print('\nOutput data:')
print(torch.reciprocal(data))