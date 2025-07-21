import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
boundaries = torch.tensor([0.5, 1.5])
out = torch.bucketize(input, boundaries)
out = torch.bucketize(input, boundaries, right=True)
out = torch.bucketize(input, boundaries, out_int32=True)