import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 1)
torch.random.set_rng_state(torch.get_rng_state())