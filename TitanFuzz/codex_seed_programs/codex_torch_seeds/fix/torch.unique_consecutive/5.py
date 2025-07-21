'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([[0, 1, 1, 2, 2, 2, 3, 3, 4, 4], [0, 0, 1, 1, 2, 2, 2, 3, 3, 4]])
print(torch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None))