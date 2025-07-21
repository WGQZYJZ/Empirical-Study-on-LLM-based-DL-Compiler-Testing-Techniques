import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.FloatTensor
input = Variable(torch.randn(1, 3, 5, 5).type(dtype), requires_grad=True)
output = torch.nn.functional.local_response_norm(input, 3)