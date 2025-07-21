import torch
from torch import nn
from torch.autograd import Variable
_input = torch.randn(2, 2)
_output = torch.Tensor.new_empty(_input, (2, 2))