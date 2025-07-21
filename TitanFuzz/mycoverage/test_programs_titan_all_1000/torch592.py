import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
non_zero_count = torch.count_nonzero(input_data)
non_zero_count = torch.count_nonzero(input_data, dim=0)
non_zero_count = torch.count_nonzero(input_data, dim=1)