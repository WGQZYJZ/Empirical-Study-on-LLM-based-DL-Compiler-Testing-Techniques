import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 1, 5)
output = torch.nn.functional.max_pool1d(input, kernel_size=3, stride=2, padding=1)