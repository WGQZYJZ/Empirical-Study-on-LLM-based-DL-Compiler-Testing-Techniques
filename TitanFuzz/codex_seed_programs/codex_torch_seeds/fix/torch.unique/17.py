'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([[1, 1, 1, 1], [1, 1, 2, 2], [3, 3, 3, 3]])
print('Input Data:')
print(input_data)
print('Output:')
print(torch.unique(input_data))