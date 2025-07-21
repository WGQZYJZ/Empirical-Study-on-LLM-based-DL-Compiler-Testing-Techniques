import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5, 5)
output = torch.nn.functional.avg_pool3d(input_data, kernel_size=3, stride=2)