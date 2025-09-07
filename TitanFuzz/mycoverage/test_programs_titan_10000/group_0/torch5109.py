import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(5, 3)
uninitialized_parameter = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)