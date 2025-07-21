import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.randn(2, 3, 4), torch.randn(2, 3, 4)]
result = torch.nn.ParameterList(input_data)