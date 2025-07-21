import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 4, dtype=torch.float32, requires_grad=True)
torch.random.set_rng_state(torch.get_rng_state())
y = torch.rand(4, 4, dtype=torch.float32, requires_grad=True)