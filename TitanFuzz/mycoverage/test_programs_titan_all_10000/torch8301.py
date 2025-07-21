import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 5, 5)
output_data = torch.nn.Hardtanh(min_val=(- 2.0), max_val=2.0)(input_data)
input_data = torch.randn(1, 3, 5, 5)
output_data = torch.nn.ReLU()(input_data)