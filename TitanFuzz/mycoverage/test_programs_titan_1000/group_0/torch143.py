import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3], [1, 3, 2], [3, 2, 1]])
_output_tensor = torch.Tensor.cummax(_input_tensor, dim=1)