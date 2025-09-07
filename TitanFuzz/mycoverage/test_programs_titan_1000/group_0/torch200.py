import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 3, requires_grad=True)
torch.Tensor.abs_(_input_tensor)