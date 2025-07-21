'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([[1, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3], [1, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]])
torch.unique_consecutive(input_data, return_inverse=False, return_counts=False, dim=None)