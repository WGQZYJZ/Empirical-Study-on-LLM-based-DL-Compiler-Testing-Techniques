import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4)
lazy_conv1d = torch.nn.LazyConv1d(1, 2, 1, 0, 1, 1, True, 'zeros', None, None)
output = lazy_conv1d(input)