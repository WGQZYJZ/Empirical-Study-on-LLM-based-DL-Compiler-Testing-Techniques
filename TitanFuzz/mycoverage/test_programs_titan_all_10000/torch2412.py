import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(6, 6)
output = torch.Tensor.slogdet(_input_tensor)