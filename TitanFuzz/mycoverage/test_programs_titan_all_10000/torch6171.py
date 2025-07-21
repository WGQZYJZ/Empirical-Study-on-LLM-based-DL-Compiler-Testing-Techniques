import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10, dtype=torch.float)
output_data = torch.digamma(input_data)