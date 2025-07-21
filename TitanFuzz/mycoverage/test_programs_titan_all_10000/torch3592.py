import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 3)
(sorted_data, sorted_index) = torch.sort(input_data)