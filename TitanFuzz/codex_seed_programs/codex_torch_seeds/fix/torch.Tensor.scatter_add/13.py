'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add\ntorch.Tensor.scatter_add(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.randn(4, 4)
index = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 0]])
src = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)