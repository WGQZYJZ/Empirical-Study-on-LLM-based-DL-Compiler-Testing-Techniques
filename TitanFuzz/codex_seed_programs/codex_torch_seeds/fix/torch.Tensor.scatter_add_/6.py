'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(3, 5)
print(input_tensor)
index = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 3]])
src = torch.tensor([[1, 0, 1, 2], [4, 1, 2, 3]])
output = torch.Tensor.scatter_add_(input_tensor, 1, index, src)
print(output)