import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1)
torch.random.fork_rng(devices=[0, 1])