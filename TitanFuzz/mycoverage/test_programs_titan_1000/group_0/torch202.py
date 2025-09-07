import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.rand(100, 10)
x2 = torch.rand(100, 10)
dis = torch.nn.functional.pairwise_distance(x1, x2)