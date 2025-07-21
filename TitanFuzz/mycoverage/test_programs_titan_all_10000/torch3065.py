import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, requires_grad=True)
_pinverse_tensor = torch.Tensor.pinverse(_input_tensor)
_input_tensor = torch.randn(2, 3, requires_grad=True)
_pinverse_tensor = torch.pinverse(_input_tensor)