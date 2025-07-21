import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_other_tensor = torch.rand(3, 3)
torch.Tensor.reshape_as(_input_tensor, _other_tensor)