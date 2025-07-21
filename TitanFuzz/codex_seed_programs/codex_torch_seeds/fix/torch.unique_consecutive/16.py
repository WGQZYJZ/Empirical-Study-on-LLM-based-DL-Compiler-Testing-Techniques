'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 8, 8, 8, 8, 8])
(unique, indices) = torch.unique_consecutive(input, return_inverse=True)
print(unique)
print(indices)
(unique, indices, counts) = torch.unique_consecutive(input, return_inverse=True, return_counts=True)
print(unique)
print(indices)
print(counts)