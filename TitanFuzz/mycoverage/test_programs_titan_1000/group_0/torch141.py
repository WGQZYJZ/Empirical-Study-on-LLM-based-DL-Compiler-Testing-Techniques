import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
output = torch.nn.functional.hardtanh_(input, min_val=(- 1.0), max_val=1.0)