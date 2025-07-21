import torch
from torch import nn
from torch.autograd import Variable
vec = torch.randn(10)
parameters = [torch.randn(2, 3, requires_grad=True), torch.randn(4, requires_grad=True)]
torch.nn.utils.vector_to_parameters(vec, parameters)