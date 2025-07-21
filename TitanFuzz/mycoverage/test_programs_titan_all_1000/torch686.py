import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5)
torch.set_rng_state(torch.get_rng_state())