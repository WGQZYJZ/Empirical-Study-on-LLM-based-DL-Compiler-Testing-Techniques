import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.arange(1, 11)
torch.Tensor.as_strided(_input_tensor, (2, 5), (5, 1))