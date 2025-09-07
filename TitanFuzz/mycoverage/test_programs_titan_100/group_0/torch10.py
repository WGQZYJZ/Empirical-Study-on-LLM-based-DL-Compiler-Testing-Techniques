import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
(min_value, min_index) = torch.min(input, 1)