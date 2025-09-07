import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.rand(1, 2), torch.rand(3, 4)]
param_list = torch.nn.ParameterList(input_data)