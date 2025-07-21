import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1)
torch.set_rng_state(torch.get_rng_state())
x = torch.randn(1)