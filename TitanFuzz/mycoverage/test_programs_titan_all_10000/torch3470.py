import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[0.5, 0.5, 0.5], [1, 1, 1], [2, 2, 2]])
_output_tensor = torch.Tensor.flipud(_input_tensor)