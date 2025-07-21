import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn((4, 4), requires_grad=True)
torch.Tensor.is_shared(_input_tensor)