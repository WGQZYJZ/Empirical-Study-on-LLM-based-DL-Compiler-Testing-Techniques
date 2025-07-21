import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
rng_state = torch.random.get_rng_state()
torch.random.set_rng_state(rng_state)
torch.random.set_rng_state(rng_state)