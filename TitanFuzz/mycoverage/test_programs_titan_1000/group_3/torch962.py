import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
abs_transform = torch.distributions.transforms.AbsTransform(cache_size=0)