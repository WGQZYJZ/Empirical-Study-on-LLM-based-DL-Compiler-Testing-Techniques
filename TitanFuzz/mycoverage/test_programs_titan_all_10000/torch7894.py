import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.tensor([1, 3, 4, 5, 6, 8, 9])
values = torch.tensor([1, 4, 6, 7, 10])
result = torch.searchsorted(sorted_sequence, values, right=True)