'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(3, 3)
index = torch.tensor([0, 1, 2, 0, 1, 2])
src = torch.tensor([1, 1, 1, 1, 1, 1])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)
print(output_tensor)