import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 3)
result = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)