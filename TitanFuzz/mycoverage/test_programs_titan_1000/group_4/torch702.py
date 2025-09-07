import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.nn.functional.threshold(input, 0.5, 0)