import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4, 5)
torch.Tensor.slogdet(_input_tensor)