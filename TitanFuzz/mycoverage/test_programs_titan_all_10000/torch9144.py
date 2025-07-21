import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
dist = torch.nn.functional.pdist(input, p=2)
dist = torch.nn.functional.pdist(input, p=1)
dist = torch.nn.functional.pdist(input, p=3)
dist = torch.nn.functional.pdist(input, p=4)