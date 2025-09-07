import torch
from torch import nn
from torch.autograd import Variable

input = torch.randint(0, 10, (10,))
counts = torch.bincount(input)
weights = torch.rand(10)
counts = torch.bincount(input, weights)
counts = torch.bincount(input, weights, minlength=10)