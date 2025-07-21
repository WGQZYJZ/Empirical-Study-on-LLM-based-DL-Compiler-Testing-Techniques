import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
rng_state = torch.random.get_rng_state()