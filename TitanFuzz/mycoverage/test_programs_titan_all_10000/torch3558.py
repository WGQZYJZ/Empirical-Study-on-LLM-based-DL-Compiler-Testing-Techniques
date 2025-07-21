import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.arange(1, 10, 2)
values = torch.tensor([1.5, 4.5])
index = torch.searchsorted(sorted_sequence, values)
index = torch.searchsorted(sorted_sequence, values, right=True)
index = torch.searchsorted(sorted_sequence, values, right=False, out_int32=True)
index = torch.searchsorted(sorted_sequence, values, right=True, out_int32=True)
index = torch.searchsorted(sorted_sequence, values, right=False, out_int32=False)
index = torch.searchsorted(sorted_sequence, values, right=True, out_int32=False)