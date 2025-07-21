'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.ones(2, 3)
print('input_tensor: ', input_tensor)
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
print('index: ', index)
src = torch.tensor([[2, 3, 4], [5, 6, 7]])
print('src: ', src)
input_tensor.scatter_add_(dim=0, index=index, src=src)
print('output: ', input_tensor)