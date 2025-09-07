import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 2)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)