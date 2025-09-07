import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.float_power_(_input_tensor, 2)