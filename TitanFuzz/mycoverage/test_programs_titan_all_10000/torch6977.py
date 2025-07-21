import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(4, 2, 3)
reshape = torch.distributions.transforms.ReshapeTransform(in_shape=(4, 2, 3), out_shape=(3, 8))