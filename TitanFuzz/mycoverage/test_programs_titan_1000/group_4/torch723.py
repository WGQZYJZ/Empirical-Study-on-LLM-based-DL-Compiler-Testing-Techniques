import torch
from torch import nn
from torch.autograd import Variable
n = 2
input = torch.randn(1, 2, dtype=torch.float64)
output = torch.special.polygamma(n, input)
n = 2
input = torch.randn(1, 2, dtype=torch.float64)
output = torch.special.polygamma(n, input)
n = 2
input = torch.randn(1, 2, dtype=torch.float64)
output = torch.special.polygamma(n, input)