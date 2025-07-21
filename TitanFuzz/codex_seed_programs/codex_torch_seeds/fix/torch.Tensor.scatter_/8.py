'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 1, 0], [0, 2, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)
print('input_tensor: ', input_tensor)
print('index: ', index)
print('src: ', src)
print('output: ', torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src))