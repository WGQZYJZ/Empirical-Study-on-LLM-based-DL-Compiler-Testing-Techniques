import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 9).view(1, 1, 9).float()
adaptive_max_pool_1d = torch.nn.AdaptiveMaxPool1d(3)
output = adaptive_max_pool_1d(data)