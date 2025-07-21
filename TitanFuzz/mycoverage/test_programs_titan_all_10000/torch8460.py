import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(5, 3)
_zero_tensor = torch.Tensor.zero_(_input_tensor)