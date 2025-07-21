import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 4, 4, 4)
output = torch.nn.functional.avg_pool3d(input, kernel_size=2, stride=2)