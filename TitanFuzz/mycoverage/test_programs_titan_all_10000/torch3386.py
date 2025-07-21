import torch
from torch import nn
from torch.autograd import Variable
sorted_sequence = torch.arange(10, dtype=torch.float)
values = torch.tensor([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
out_int32 = torch.searchsorted(sorted_sequence, values, out_int32=True)
out_int64 = torch.searchsorted(sorted_sequence, values, out_int32=False)
out_right = torch.searchsorted(sorted_sequence, values, right=True)