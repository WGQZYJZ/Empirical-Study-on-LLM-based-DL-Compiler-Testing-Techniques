import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5, 5))
output = torch.nn.functional.adaptive_max_pool3d(input, output_size=(1, 1, 1))