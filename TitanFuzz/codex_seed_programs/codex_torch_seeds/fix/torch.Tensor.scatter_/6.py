'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
_input_tensor = torch.randn(4, 3)
print(_input_tensor)
_dim = 0
_index = torch.tensor([0, 2])
_src = torch.tensor([[0, 0, 0], [1, 1, 1]])
_reduce = None
torch.Tensor.scatter_(_input_tensor, _dim, _index, _src, _reduce)
print(_input_tensor)