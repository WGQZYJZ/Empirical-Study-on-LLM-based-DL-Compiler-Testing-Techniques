import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 3)
(max_value, max_index) = torch.max(input, dim=1)