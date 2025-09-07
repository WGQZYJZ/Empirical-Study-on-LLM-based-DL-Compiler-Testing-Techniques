import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(100, 100)
torch.Tensor.sgn_(_input_tensor)