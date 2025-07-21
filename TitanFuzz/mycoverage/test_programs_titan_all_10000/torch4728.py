import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2)
uninitialized_parameter = torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)