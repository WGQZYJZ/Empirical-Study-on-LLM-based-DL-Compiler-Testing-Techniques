import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
output = torch.nn.functional.hardtanh_(input_data, min_val=(- 1), max_val=1)