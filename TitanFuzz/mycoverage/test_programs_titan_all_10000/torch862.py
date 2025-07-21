import torch
from torch import nn
from torch.autograd import Variable
_input_data = torch.rand(4, 4)
mean_value = torch.Tensor.mean(_input_data, dim=1)