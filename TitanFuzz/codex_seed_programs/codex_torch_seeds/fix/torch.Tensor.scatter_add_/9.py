'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_add_\ntorch.Tensor.scatter_add_(_input_tensor, dim, index, src)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.Tensor.scatter_add_')
print('torch.Tensor.scatter_add_(_input_tensor, dim, index, src)')
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
index = torch.tensor([[0, 1], [1, 0]])
src = torch.tensor([[1, 2], [3, 4]])
print('input tensor: ', input_tensor)
print('index tensor: ', index)
print('src tensor: ', src)
print('scatter_add_: ', input_tensor.scatter_add_(0, index, src))