'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagflat\ntorch.diagflat(input, offset=0)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.diagflat(input)
print('input:')
print(input)
print('output:')
print(output)