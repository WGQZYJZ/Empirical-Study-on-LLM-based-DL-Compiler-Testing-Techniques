import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
indices = torch.triu_indices(4, 4, 0)
output = torch.triu(input_data, 0)