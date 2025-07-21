import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, requires_grad=True)
torch.jit.unused(x)