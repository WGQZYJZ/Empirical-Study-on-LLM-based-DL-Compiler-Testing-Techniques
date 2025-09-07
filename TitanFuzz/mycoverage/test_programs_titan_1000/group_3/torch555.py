import torch
from torch import nn
from torch.autograd import Variable
torch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')