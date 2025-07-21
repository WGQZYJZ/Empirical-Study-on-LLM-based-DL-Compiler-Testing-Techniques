'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
_input_tensor = torch.rand(3, 4)
dim = 0
index = torch.tensor([0, 2])
src = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
print(_input_tensor)
print(torch.Tensor.scatter_add(_input_tensor, dim, index, src))