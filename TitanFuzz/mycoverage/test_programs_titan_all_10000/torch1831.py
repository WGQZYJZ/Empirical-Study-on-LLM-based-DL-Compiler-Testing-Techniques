import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 10, 10, 10)
pool = torch.nn.AdaptiveAvgPool3d(output_size=(5, 5, 5))
output = pool(Variable(input))