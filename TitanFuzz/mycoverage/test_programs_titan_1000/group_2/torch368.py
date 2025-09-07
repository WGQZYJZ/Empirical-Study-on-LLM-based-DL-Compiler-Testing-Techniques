import torch
from torch import nn
from torch.autograd import Variable
parameter_dict = torch.nn.ParameterDict(parameters={'parameter1': torch.nn.Parameter(torch.randn(2, 3)), 'parameter2': torch.nn.Parameter(torch.randn(5, 7))})