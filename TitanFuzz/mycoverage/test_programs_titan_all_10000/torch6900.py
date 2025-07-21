import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.is_set_to(_input_tensor, torch.randn(2, 3))