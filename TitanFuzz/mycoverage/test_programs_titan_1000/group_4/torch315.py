import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 3, 4, 4)
output = torch.nn.functional.mish(input)