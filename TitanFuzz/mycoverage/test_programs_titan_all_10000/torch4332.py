import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 2)
state_before = torch.get_rng_state()
data = torch.randn(1, 2)
state_after = torch.get_rng_state()
torch.set_rng_state(state_before)
data = torch.randn(1, 2)
state_after = torch.get_rng_state()