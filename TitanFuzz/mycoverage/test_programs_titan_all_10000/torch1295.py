import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 2, 2, 2))
output = torch.nn.functional.adaptive_max_pool3d(input_data, (1, 1, 1))