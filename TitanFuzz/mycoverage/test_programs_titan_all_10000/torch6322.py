import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3)
cos_output = torch.Tensor.cos(_input_tensor)