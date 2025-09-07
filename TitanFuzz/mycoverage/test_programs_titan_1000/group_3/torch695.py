import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.arange(1, 21).view(4, 5)
_output_tensor = torch.Tensor.as_strided(_input_tensor, (3, 4), (5, 1))