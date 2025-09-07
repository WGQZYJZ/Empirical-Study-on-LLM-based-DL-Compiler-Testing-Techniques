import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.get_rng_state()