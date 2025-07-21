import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 0, 0, 1, 1], [0, 0, 1, 0, 1]])
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)