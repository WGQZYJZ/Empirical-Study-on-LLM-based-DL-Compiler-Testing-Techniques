'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
input = torch.tensor([[1, torch.nan, 3], [4, 5, torch.nan]])
print('Input: ', input)
output = torch.nan_to_num(input)
print('Output: ', output)