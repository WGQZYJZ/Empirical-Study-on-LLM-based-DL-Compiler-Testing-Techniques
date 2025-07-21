'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique\ntorch.Tensor.unique(_input_tensor, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15])
unique_tensor = input_tensor.unique(sorted=True, return_inverse=False, return_counts=False, dim=None)
print('Input tensor:')
print(input_tensor)
print('Unique tensor:')
print(unique_tensor)