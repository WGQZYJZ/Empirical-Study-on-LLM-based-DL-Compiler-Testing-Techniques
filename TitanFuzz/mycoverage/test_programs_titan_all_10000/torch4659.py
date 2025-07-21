import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4, 5)
sum_to_size_output = torch.Tensor.sum_to_size(_input_tensor, 2, 3, 4, 5)