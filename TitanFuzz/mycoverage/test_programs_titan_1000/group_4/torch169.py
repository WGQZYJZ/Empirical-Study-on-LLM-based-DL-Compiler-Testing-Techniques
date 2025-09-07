import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
tanh_transform = torch.distributions.transforms.TanhTransform(cache_size=0)