import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn((1, 2, 3, 4))
torch._assert((x.shape == (1, 2, 3, 4)), 'x.shape is not (1, 2, 3, 4)')