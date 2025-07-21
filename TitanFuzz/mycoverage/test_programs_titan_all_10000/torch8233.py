import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 10, 10)
output = torch.nn.functional.adaptive_avg_pool2d(input, output_size=(2, 2))