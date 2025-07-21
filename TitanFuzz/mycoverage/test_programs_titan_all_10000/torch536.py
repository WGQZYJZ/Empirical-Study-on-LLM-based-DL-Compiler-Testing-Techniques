import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.get_device(_input_tensor)