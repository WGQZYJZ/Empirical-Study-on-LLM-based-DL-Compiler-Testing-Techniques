'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
import torch
data = torch.randn(3, 4)
print('data: ', data)
index = torch.tensor([1, 2])
print('index: ', index)
src = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('src: ', src)
torch.Tensor.scatter_(data, dim=0, index=index, src=src)
print('output: ', data)