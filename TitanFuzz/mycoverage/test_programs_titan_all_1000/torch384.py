import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3, 5, 7)
torch.Tensor.sgn_(_input_tensor)