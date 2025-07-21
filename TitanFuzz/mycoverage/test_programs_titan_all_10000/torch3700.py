import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(5, 5)
trans = torch.distributions.transforms.TanhTransform(cache_size=0)