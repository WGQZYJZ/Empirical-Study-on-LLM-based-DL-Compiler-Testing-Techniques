import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
rng_state = torch.get_rng_state()
torch.set_rng_state(rng_state)