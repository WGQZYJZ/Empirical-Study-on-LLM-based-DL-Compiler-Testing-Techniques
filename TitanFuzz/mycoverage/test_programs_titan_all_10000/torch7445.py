import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[True, True], [True, False], [False, True], [False, False]])
result = torch.Tensor.logical_xor(input_data, input_data)