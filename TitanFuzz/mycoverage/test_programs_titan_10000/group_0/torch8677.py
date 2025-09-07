import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(2, 3)
torch.random.set_rng_state(torch.get_rng_state())
output_data = torch.rand(2, 3)