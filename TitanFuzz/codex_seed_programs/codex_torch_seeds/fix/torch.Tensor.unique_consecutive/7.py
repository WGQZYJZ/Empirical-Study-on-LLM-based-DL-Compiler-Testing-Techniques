'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique_consecutive\ntorch.Tensor.unique_consecutive(_input_tensor, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3], [1, 2, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3]])
result = torch.Tensor.unique_consecutive(input_tensor, return_inverse=False, return_counts=False, dim=None)
print(result)