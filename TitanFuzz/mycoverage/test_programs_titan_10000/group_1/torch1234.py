import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(3, 3)
_result = torch.Tensor.int_repr(_input_tensor)