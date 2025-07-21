import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4, 4)
pool = torch.nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))
output = pool(input)