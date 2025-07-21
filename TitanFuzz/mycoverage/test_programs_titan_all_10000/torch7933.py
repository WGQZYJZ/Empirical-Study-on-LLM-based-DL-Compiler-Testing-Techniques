import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5)
output_data = torch.nn.functional.hardtanh(input_data)