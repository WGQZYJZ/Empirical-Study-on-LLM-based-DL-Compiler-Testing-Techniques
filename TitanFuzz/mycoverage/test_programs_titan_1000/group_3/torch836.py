import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
tanh_transform = torch.distributions.transforms.TanhTransform(cache_size=0)