import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 1, 3, 3)
torch.Tensor.q_scale(_input_tensor)