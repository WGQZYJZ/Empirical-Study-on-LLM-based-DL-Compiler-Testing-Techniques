import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False], [True, True]])
other = torch.tensor([[True, False], [False, True]])
torch.Tensor.logical_xor_(input_tensor, other)