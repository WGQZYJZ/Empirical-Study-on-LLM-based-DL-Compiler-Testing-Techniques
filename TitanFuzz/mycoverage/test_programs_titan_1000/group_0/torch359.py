import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
torch.random.set_rng_state(torch.get_rng_state())
y = torch.randn(1, requires_grad=True)
z = (x + y)
z.backward()