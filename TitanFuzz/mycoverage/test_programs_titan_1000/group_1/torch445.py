import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(20, 16, 50, 32, 45)
output_size = (1, 1, 1)
avg_pool_3d = torch.nn.AdaptiveAvgPool3d(output_size)
output = avg_pool_3d(input_data)