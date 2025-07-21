import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(5, 3)
_absolute_tensor = torch.Tensor.absolute_(_input_tensor)