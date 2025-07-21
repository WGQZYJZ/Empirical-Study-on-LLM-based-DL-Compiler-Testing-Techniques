import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.arange(10)
values = torch.tensor([2, 3, 5, 7, 8, 9])
torch.searchsorted(sorted_sequence, values, right=False)
sorted_sequence = torch.arange(10)
values = torch.tensor([2, 3, 5, 7, 8, 9])
torch.searchsorted(sorted_sequence, values, right=True)