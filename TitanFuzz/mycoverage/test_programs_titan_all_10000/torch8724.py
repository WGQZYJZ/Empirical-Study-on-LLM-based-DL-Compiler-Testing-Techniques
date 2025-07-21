import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10, 10)
uninitialized_buffer = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)