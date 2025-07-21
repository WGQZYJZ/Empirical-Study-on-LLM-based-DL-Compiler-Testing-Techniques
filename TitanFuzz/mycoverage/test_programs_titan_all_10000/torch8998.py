import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
torch.set_rng_state(torch.get_rng_state())