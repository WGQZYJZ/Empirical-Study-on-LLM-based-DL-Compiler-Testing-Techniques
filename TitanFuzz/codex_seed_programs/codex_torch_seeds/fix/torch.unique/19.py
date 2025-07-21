'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([1, 3, 2, 3, 1])
output = torch.unique(input)
print('Output:', output)
(output, inverse_indices) = torch.unique(input, return_inverse=True)
print('Output:', output)
print('Inverse Indices:', inverse_indices)
(output, inverse_indices, counts) = torch.unique(input, return_inverse=True, return_counts=True)
print('Output:', output)
print('Inverse Indices:', inverse_indices)
print('Counts:', counts)