import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.randn(2, 3)
detach_output = torch.Tensor.detach(_input_tensor)