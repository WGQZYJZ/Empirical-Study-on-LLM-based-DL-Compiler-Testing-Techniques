import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
(mode_value, mode_idx) = torch.mode(input_data, dim=(- 1), keepdim=False, out=None)