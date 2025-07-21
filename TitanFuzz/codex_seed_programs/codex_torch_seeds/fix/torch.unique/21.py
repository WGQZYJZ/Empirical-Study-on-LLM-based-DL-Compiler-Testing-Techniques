'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([[1, 3, 3, 2, 1], [1, 3, 2, 1, 3]])
print('Input: ', input)
(unique_output, inverse_output, count_output) = torch.unique(input, sorted=True, return_inverse=True, return_counts=True, dim=0)
print('Unique Output: ', unique_output)
print('Inverse Output: ', inverse_output)
print('Count Output: ', count_output)