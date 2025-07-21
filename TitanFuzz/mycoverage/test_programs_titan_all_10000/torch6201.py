import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.tensor([[1, 2], [3, 4]])
x2 = torch.tensor([[1, 1], [4, 4]])
output = torch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)
output = torch.nn.functional.pairwise_distance(x1, x2, p=1.0, eps=1e-06, keepdim=False)