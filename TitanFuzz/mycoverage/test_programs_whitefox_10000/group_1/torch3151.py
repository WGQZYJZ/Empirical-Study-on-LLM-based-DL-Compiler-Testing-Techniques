import torch
from torch import nn

x = torch.cat([x, x], dim=3)
x = torch.tanh(x)
