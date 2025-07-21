import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 5)
(max_value, max_idx) = torch.max(input_data, dim=1)
(max_value, max_idx) = torch.max(input_data, dim=1, keepdim=True)
(max_value, max_idx) = torch.max(input_data, dim=0, keepdim=True)