import torch
from torch import nn
from torch.autograd import Variable
parameters = [torch.randn(1, 2, 3), torch.randn(4, 5, 6)]
parameters_vector = torch.nn.utils.parameters_to_vector(parameters)