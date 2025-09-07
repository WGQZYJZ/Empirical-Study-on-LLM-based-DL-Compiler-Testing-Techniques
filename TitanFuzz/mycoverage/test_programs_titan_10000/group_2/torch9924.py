import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(10, 3)
dist = torch.nn.functional.pdist(x)