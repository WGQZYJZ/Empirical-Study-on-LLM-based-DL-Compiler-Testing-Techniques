import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
p = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)