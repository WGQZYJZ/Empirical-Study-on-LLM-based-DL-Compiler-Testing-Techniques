import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(3, 5)
y = torch.randn(3, 5)
dist = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)