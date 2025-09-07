import torch
from torch import nn
from torch.autograd import Variable

input_size = (3, 4)
input_data = torch.randn(input_size)
parameter_dict = torch.nn.ParameterDict(parameters=None)