import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
parameter_dict = torch.nn.ParameterDict(parameters=None)
parameter_dict['input_data'] = input_data