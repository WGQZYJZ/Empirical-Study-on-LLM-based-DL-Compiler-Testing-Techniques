'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
input_tensor = torch.rand(4, 3)
print('input_tensor: ', input_tensor)
output_tensor = torch.zeros(4, 3)
print('output_tensor: ', output_tensor)
dim = 0
index = torch.tensor([0, 2, 1, 0])
src = torch.tensor([1, 2, 3, 4])
print('dim: ', dim)
print('index: ', index)
print('src: ', src)
output_tensor.scatter_(dim, index, src)
print('output_tensor: ', output_tensor)