import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 4)
y = torch.rand(4, 4)
torch._assert((x.shape == y.shape), 'shape mismatch')