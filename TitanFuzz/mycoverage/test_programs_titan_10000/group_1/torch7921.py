import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(3, requires_grad=True)
torch._assert((x.shape[0] == 3), 'x must have 3 elements')