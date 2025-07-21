'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
_input_tensor = torch.randn(3, 4)
_dim = 0
_index = torch.tensor([1, 1, 2, 2])
_src = torch.tensor([1, 2, 3, 4])
_reduce = None
_output_tensor = torch.Tensor.scatter_(_input_tensor, _dim, _index, _src, _reduce)
print(_output_tensor)