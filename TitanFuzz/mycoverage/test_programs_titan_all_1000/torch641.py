import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False, False, False], [True, True, True, True]])
other = torch.tensor([[True, True, True, True], [True, False, False, False]])
torch.Tensor.bitwise_or_(input_tensor, other)