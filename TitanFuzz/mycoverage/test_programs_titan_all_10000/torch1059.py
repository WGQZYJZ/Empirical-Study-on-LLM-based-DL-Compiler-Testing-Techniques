import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(4, 16, 32, 32, 32)
avg_pool3d_output = torch.nn.functional.avg_pool3d(input_data, kernel_size=3, stride=1, padding=1)