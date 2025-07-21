import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5)
tanh_trans = torch.distributions.transforms.TanhTransform(cache_size=0)
y = tanh_trans(x)