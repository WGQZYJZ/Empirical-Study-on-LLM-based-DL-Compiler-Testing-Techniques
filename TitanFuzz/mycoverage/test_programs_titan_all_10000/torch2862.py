import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
_output_tensor = torch.Tensor.new_zeros(_input_tensor, (2, 3))