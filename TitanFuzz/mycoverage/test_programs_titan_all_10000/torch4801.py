import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 5)
output_data = torch.diag(input_data)