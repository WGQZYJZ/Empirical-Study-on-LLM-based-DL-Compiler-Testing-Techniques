import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10)
sigmoid = torch.distributions.transforms.SigmoidTransform(cache_size=0)