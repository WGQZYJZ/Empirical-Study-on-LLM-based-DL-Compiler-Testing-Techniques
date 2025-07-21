import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
boundaries = torch.tensor([0.5, 1.5])
out = torch.bucketize(input, boundaries)
input = torch.randn(3, 4)
chunks = 2
out = torch.chunk(input, chunks, dim=0)