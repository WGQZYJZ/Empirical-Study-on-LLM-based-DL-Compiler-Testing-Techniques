'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique_consecutive\ntorch.Tensor.unique_consecutive(_input_tensor, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3]])
print(torch.Tensor.unique_consecutive(input_tensor))
print(torch.Tensor.unique_consecutive(input_tensor, return_inverse=True))
print(torch.Tensor.unique_consecutive(input_tensor, return_counts=True))
print(torch.Tensor.unique_consecutive(input_tensor, dim=0))
print(torch.Tensor.unique_consecutive(input_tensor, return_inverse=True, dim=0))
print(torch.Tensor.unique_consecutive(input_tensor, return_counts=True, dim=0))