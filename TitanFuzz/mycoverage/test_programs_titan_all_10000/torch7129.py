import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
(max_value, max_index) = torch.max(input, dim=1)