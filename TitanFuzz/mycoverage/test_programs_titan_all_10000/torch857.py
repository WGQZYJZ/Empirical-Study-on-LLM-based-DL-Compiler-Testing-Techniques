import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
_flip_tensor = torch.Tensor.flip(_input_tensor, (1,))