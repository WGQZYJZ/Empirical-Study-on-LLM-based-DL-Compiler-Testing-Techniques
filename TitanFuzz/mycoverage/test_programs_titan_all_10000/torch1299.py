import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5)
adaptive_avg_pool1d = torch.nn.AdaptiveAvgPool1d(output_size=1)
output_data = adaptive_avg_pool1d(input_data)