'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [2, 3, 4]])
print(x)
print(torch.unique_consecutive(x))
print(torch.unique_consecutive(x, return_inverse=True, return_counts=True))