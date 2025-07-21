import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, dtype=torch.float32)
output = torch.special.i0e(input_data)