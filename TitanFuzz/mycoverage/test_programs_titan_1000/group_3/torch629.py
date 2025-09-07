import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 4, 4, 4))
avg_pool3d = torch.nn.AdaptiveAvgPool3d(output_size=(1, 1, 1))
output = avg_pool3d(input)