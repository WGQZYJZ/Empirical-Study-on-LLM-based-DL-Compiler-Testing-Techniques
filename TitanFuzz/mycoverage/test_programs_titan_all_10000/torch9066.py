import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(4, 4)
boundaries = torch.tensor([0.2, 0.6])
bucketized_tensor = torch.bucketize(input, boundaries)
input = torch.tensor([1, 2, 4, 4, 2, 1])
bincount = torch.bincount(input)