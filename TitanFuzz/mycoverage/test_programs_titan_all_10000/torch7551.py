import torch
from torch import nn
from torch.autograd import Variable
vec = torch.randn(10)
parameters = [torch.randn(2, 3), torch.randn(1, 2)]
torch.nn.utils.vector_to_parameters(vec, parameters)
for parameter in parameters:
    print(parameter)