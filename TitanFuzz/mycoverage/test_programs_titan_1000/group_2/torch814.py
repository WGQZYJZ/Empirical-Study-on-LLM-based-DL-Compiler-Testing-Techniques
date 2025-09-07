import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 1, 2, 2, 2)
output = torch.nn.functional.avg_pool3d(input, kernel_size=2)