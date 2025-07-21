import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[1, 2], [3, 4]])
pairwise_distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
distance = pairwise_distance(x, y)