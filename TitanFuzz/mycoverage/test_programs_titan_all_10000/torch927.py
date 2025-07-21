import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
input_data[(0, 1)] = float('nan')
input_data[(1, 2)] = float('nan')
output = torch.nanmean(input_data, dim=0, keepdim=False)