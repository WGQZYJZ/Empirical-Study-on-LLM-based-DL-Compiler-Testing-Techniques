'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input = torch.tensor([[1, 1, 1, 2, 2, 3, 3, 3, 3, 3]])
output = torch.unique_consecutive(input, return_inverse=True, return_counts=True)
print(output)