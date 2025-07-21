import torch
from torch import nn
from torch.autograd import Variable
tensor_input = torch.randn(2, 3, 4)
split_size_or_sections = 2
dim = 1
result = torch.split(tensor_input, split_size_or_sections, dim)