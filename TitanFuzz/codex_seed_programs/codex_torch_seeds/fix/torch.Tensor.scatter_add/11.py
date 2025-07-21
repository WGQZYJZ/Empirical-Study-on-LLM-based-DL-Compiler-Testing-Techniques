'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
import torch
input_tensor = torch.rand(4, 3)
print('input_tensor:', input_tensor)
index = torch.tensor([0, 2, 1, 2])
src = torch.tensor([1.0, 2.0, 3.0, 4.0])
output_tensor = torch.Tensor.scatter_add(input_tensor, 0, index, src)
print('output_tensor:', output_tensor)