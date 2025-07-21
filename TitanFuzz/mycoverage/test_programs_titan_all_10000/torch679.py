import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False], [False, True]])
result = torch.Tensor.logical_xor(input_tensor, other=True)