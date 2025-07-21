import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, requires_grad=True)
torch.Tensor.retains_grad(_input_tensor)