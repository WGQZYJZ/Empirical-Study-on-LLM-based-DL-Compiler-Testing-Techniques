import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, dtype=torch.float)
output_data = torch.erfinv(input_data)