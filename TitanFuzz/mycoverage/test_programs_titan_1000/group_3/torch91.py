import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 8, 8, 8))
output = torch.nn.functional.adaptive_max_pool3d(input, (4, 4, 4))