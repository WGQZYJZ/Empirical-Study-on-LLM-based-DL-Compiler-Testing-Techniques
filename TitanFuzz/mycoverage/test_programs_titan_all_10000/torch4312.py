import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
output_data = torch.cosh(input_data)
input_data = torch.randn(3, 4)
output_data = torch.erf(input_data)
input_data = torch.randn(3, 4)
output_data = torch.erfc(input_data)