import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 5)
(sorted_data, sorted_indices) = torch.sort(input)
(sorted_data, sorted_indices) = torch.sort(input, dim=0)
(sorted_data, sorted_indices) = torch.sort(input, dim=1)