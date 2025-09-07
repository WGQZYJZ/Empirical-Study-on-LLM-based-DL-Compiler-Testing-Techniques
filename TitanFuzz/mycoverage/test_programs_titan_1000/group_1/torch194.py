import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 5)
_index_tensor = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 4]])
_src_tensor = torch.tensor([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]])
_output_tensor = torch.Tensor.scatter_(_input_tensor, 0, _index_tensor, _src_tensor)