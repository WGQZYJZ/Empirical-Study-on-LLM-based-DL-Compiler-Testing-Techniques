import torch
from torch import nn
from torch.autograd import Variable
p1 = torch.randn(3, 3)
p2 = torch.randn(3, 3)
p3 = torch.randn(3, 3)
parameters = [p1, p2, p3]
vector = torch.nn.utils.parameters_to_vector(parameters)