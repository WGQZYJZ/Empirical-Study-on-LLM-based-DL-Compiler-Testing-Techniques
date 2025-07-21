import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
output = torch.nn.functional.celu(input, alpha=1.0, inplace=False)