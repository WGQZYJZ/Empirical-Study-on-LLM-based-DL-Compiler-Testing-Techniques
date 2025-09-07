import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 3)
other_data = torch.randn(2, 3)
out_data = torch.ne(input_data, other_data)