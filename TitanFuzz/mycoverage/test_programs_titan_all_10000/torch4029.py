import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
trace_tensor = torch.trace(input_tensor)
input_variable = Variable(input_tensor, requires_grad=True)
trace_variable = torch.trace(input_variable)