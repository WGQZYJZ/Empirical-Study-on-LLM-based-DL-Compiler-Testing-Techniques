import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[True, False], [False, True]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other=True)