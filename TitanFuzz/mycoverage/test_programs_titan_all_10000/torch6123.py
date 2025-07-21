import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, 3)
(sorted_input, sorted_indices) = torch.sort(input, dim=1, descending=False)
(sorted_input, sorted_indices) = torch.sort(input, dim=0, descending=False)