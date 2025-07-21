'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.take\ntorch.take(input, index)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('input:', input)
index = torch.tensor([[0, 1], [1, 2]])
print('index:', index)
print('torch.take(input, index):', torch.take(input, index))