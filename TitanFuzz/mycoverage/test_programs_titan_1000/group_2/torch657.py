import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1)
new_state = torch.get_rng_state()
torch.random.set_rng_state(new_state)
y = torch.rand(1)