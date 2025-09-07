import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.randn(2, 2)
torch.Tensor.data_ptr(_input_tensor)