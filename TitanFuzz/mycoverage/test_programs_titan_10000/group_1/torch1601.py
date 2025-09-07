import torch
from torch import nn
from torch.autograd import Variable

input_data = Variable(torch.randn(1, 1, 4, 4))
output = torch.nn.functional.adaptive_max_pool2d(input_data, (1, 1))