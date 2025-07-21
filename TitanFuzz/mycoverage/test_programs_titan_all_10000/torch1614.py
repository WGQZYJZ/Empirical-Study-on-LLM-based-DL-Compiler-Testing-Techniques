import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1)
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())
torch.random.manual_seed(1)
torch.random.initial_seed()
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())