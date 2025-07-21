import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
(max_value, max_index) = torch.max(input, 1)