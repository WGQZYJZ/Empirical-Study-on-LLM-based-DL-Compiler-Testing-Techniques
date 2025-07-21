import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2)
output_data = torch.special.logsumexp(input_data, dim=1, keepdim=False)