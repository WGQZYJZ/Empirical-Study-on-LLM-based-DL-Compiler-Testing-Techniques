import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(3, 2)
uninitialized_buffer = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)