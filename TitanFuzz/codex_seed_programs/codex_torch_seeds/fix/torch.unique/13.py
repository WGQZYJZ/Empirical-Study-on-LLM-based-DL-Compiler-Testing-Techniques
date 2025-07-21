'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([[1, 0, 0, 1, 1], [1, 1, 0, 0, 1]])
(unique_input, inverse_input, counts_input) = torch.unique(input, return_inverse=True, return_counts=True)
print(unique_input)
print(inverse_input)
print(counts_input)