import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.zeros(3, 3)
torch.Tensor.fill_(_input_tensor, 3.14)