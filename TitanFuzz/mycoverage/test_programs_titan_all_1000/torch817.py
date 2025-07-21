import torch
from torch import nn
from torch.autograd import Variable
input_data = {'param1': torch.randn(2, 3), 'param2': torch.randn(2, 3)}
parameter_dict = torch.nn.ParameterDict(parameters=input_data)