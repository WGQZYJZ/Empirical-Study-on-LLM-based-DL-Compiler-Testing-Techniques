'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
input = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print('Input: ', input)
output = torch.squeeze(input)
print('Output: ', output)