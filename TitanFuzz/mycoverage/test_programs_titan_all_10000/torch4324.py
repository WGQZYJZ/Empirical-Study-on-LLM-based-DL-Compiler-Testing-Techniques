import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(10, 10)
torch.Tensor.sinc_(_input_tensor)