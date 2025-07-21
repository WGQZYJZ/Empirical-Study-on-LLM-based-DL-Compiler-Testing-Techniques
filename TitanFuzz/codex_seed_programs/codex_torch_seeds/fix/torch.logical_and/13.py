'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
input = torch.tensor([[1, 0, 1], [1, 1, 0], [0, 0, 0]], dtype=torch.bool)
other = torch.tensor([[1, 1, 1], [1, 0, 1], [0, 0, 1]], dtype=torch.bool)
print('Input:')
print(input)
print('Other:')
print(other)
output = torch.logical_and(input, other)
print('Output:')
print(output)