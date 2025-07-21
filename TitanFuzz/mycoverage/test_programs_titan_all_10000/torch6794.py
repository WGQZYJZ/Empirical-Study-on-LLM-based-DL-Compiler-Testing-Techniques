import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
_squeeze_tensor = torch.Tensor.squeeze(_input_tensor, dim=None)