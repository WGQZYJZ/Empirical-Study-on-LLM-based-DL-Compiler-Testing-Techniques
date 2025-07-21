import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.ByteTensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]])
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)