import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4, 5)
_element_size = torch.Tensor.element_size(_input_tensor)