import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.arange(10)
values = torch.tensor([3, 4, 1, 8])
result = torch.searchsorted(sorted_sequence, values)