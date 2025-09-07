import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False, True], [False, True, False], [True, False, True]])
other = torch.tensor([[True, True, True], [True, True, True], [True, True, True]])
output_tensor = torch.Tensor.logical_or(input_tensor, other)