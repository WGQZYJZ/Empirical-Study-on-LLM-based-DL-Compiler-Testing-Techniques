import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 1)
transform = torch.distributions.transforms.ExpTransform(cache_size=0)