import torch
from torch import nn
from torch.autograd import Variable
a = torch.rand(2, 3)
torch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')