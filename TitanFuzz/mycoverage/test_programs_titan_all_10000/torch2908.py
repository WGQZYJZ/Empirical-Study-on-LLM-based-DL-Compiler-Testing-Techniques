import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, float('nan'), 3])
output = torch.isnan(input)
input = torch.tensor([1, float('inf'), 3])
output = torch.isinf(input)
input = torch.tensor([1, float('inf'), 3])