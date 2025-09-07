import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 4)
b = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)