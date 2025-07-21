import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3, 5)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))