import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
_result = torch.Tensor.is_inference(_input_tensor)