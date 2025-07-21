import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4, 4))
pool = torch.nn.AdaptiveMaxPool3d((2, 2, 2))
output = pool(input)