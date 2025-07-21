'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensordot\ntorch.tensordot(a, b, dims=2, out=None)\n'
import torch
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[1, 2], [3, 4]])
print('a: ', a)
print('b: ', b)
print('a.shape: ', a.shape)
print('b.shape: ', b.shape)
print('a.size: ', a.size())
print('b.size: ', b.size())
print('torch.tensordot(a,b,dims=2,out=None): ', torch.tensordot(a, b, dims=2, out=None))
print('torch.tensordot(a,b,dims=1,out=None): ', torch.tensordot(a, b, dims=1, out=None))