import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3)
output_size = (2,)
output = torch.nn.functional.adaptive_avg_pool1d(input, output_size)