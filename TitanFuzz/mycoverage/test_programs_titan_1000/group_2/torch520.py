import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.randn(10)
values = torch.randn(5)
result = torch.searchsorted(sorted_sequence, values)