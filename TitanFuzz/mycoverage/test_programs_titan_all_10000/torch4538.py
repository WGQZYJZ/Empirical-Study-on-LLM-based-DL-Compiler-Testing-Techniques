import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
_input_tensor = torch.randn(3, 4)
_dim = (- 1)
_descending = False
output_tensor = torch.Tensor.sort(_input_tensor, _dim, _descending)