import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, float('nan')], [float('inf'), float('-inf')]])
output = torch.nan_to_num(input)