import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(5, 3)
y = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)