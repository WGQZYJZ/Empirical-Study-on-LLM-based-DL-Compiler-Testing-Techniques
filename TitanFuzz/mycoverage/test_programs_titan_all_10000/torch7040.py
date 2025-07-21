import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
(sorted_input, sorted_index) = torch.sort(input, dim=0)