import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.ones(2, 3)
_result = torch.Tensor.divide(_input_tensor, 2)