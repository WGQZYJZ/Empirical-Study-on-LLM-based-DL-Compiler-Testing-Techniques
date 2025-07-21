import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 5, 5, 5)
output = torch.nn.functional.avg_pool3d(input, kernel_size=3, stride=1)