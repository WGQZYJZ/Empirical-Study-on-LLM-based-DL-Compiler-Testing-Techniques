import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 1)
_output_tensor = torch.Tensor.broadcast_to(_input_tensor, (4, 3))