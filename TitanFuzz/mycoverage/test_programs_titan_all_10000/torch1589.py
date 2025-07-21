import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5)
boundaries = torch.tensor([0.0, 1.0])
torch.bucketize(input, boundaries)