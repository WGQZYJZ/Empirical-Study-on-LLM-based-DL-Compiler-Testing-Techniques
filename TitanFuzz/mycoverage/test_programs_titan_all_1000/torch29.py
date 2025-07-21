import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4, 4)
avg_pool3d = torch.nn.functional.avg_pool3d(input, kernel_size=(2, 2, 2))