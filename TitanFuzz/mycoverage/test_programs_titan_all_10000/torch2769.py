import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5)
avg_pool1d = torch.nn.AdaptiveAvgPool1d(output_size=3)
output = avg_pool1d(input_data)