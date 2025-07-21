import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(1, 1, 10)
output = torch.nn.functional.adaptive_avg_pool1d(data, output_size=3)