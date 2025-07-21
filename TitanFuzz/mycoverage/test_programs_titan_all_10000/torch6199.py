import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))