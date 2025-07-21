import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2)
rng_state = torch.get_rng_state()