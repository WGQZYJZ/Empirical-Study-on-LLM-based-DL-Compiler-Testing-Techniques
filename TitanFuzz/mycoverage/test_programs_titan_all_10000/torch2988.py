import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 2, 2)
parameters = [torch.ones(2, 2, requires_grad=True), torch.ones(1, 1, requires_grad=True)]
vec = torch.cat([p.data.view((- 1)) for p in parameters])
torch.nn.utils.vector_to_parameters(vec, parameters)