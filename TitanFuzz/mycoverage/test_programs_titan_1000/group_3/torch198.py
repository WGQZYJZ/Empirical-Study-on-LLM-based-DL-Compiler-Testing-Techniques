import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 3)
transform = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)