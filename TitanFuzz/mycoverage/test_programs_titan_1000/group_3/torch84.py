import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
state = torch.random.get_rng_state()