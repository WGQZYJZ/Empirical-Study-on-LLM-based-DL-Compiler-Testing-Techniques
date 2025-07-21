import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.rand(1, 3)
x2 = torch.rand(1, 3)
pairwise_distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
distance = pairwise_distance.forward(x1, x2)