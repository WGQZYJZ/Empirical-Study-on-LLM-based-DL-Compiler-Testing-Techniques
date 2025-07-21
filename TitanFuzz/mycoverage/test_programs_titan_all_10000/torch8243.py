import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
torch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')