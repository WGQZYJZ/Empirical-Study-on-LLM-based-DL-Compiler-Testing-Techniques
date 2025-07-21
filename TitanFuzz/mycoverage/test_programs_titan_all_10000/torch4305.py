import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
torch.random.set_rng_state(torch.get_rng_state())