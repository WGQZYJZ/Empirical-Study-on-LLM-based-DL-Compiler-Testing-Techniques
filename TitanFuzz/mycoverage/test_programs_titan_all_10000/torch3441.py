import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1)
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())
torch.random.get_rng_state()