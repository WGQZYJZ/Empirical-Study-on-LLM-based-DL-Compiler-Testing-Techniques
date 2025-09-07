import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 2, 3, 4, 5)
torch.Tensor.is_pinned(_input_tensor)