'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cross\ntorch.Tensor.cross(_input_tensor, other, dim=-1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[4, 5, 6], [1, 2, 3]])
cross_tensor = input_tensor.cross(other)
print(cross_tensor)