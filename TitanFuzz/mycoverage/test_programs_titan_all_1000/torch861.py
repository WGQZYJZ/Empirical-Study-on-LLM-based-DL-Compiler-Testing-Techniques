import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
output_data = torch.square(input_data)
output_data = torch.sqrt(input_data)
output_data = torch.rsqrt(input_data)
output_data = torch.pow