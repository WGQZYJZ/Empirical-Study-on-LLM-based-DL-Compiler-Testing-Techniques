import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
ht = torch.nn.Hardtanh()
output = ht(input_data)