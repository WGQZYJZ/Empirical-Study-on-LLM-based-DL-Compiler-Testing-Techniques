import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 5, 5, 5))
max_pool_3d = torch.nn.AdaptiveMaxPool3d(output_size=(3, 3, 3))
output = max_pool_3d(input)