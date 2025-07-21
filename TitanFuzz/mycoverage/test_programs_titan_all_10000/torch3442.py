import torch
from torch import nn
from torch.autograd import Variable
input_data = [torch.randn(3, 4), torch.randn(2)]
output_data = torch.atleast_1d(*input_data)