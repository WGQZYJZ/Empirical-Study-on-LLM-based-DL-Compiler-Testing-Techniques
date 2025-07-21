import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3)
output_data = torch.logsumexp(input_data, dim=1, keepdim=True)