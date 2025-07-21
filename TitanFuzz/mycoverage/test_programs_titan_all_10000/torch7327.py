import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
values = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
result = torch.searchsorted(sorted_sequence, values, right=True)