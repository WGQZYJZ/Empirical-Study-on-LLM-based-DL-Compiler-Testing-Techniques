import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[True, False], [False, False]])
other_data = torch.tensor([[True, True], [False, False]])
output_data = torch.logical_or(input_data, other_data)