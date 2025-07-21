import torch
from torch import nn
from torch.autograd import Variable
_input = torch.randn(2, 3)
_output = torch.Tensor.any(_input)