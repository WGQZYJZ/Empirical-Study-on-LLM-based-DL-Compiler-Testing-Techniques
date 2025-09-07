import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
torch.random.fork_rng(devices=[0, 1], enabled=True, _caller='fork_rng', _devices_kw='devices')