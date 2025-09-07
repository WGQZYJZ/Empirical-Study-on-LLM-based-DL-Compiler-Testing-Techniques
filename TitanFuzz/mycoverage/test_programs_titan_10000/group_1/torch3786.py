import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(4, 4)
state = torch.get_rng_state()
torch.random.set_rng_state(state)
y = torch.rand(4, 4)