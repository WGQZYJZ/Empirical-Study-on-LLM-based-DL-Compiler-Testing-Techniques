import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, dtype=torch.float64)
output = torch.special.erfcx(input_data)