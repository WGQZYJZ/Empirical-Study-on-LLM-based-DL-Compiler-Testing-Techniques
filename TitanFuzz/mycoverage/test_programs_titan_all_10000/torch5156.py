import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
_output = torch.Tensor.qscheme(_input_tensor)