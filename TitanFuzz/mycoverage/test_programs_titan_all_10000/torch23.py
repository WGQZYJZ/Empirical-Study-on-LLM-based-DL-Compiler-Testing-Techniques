import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([float('NaN'), float('NaN'), float('Inf'), float('-Inf')])
output = torch.nan_to_num(input)