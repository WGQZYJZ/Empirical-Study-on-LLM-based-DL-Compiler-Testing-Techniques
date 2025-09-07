import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.randn(2, 3)
x2 = torch.randn(2, 3)
distance = torch.nn.functional.pairwise_distance(x1, x2)