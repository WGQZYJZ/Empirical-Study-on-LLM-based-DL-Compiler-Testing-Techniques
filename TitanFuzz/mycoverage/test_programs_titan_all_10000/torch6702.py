import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[True, False], [True, True]])
other = torch.tensor([[True, True], [True, False]])
torch.Tensor.bitwise_or_(_input_tensor, other)