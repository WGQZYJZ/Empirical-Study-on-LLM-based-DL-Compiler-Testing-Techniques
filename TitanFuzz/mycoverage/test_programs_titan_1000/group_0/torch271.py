import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(4, 4)
(min_value, min_index) = torch.min(input_data, dim=0, keepdim=False)
(min_value, min_index) = torch.min(input_data, dim=0, keepdim=True)