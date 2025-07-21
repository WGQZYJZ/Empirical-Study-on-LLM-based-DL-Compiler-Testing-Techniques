'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])
index = torch.tensor([[0, 1, 2], [1, 2, 3]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.scatter_add(input_tensor, 0, index, src)
print(output_tensor)