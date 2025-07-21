import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 224, 224)
output = torch.nn.functional.hardsigmoid(input)