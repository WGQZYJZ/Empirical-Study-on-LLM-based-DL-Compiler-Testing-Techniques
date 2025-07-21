'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(4, 3, 3)
index = torch.tensor([[0, 1, 2, 0], [2, 0, 0, 1]])
src = torch.tensor([[1, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0]])
output_tensor = torch.Tensor.scatter_add_(input_tensor, 1, index, src)
print(output_tensor)