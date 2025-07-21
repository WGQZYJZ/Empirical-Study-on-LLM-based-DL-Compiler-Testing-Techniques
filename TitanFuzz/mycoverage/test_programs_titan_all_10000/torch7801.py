import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
torch.Tensor.element_size(_input_tensor)
_input_tensor = torch.rand(2, 3)
torch.Tensor.numel(_input_tensor)