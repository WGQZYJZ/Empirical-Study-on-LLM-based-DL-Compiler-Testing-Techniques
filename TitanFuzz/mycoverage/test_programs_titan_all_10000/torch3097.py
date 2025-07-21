import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.rand(10, 3)
x2 = torch.rand(10, 3)
distance = torch.nn.functional.pairwise_distance(x1, x2)