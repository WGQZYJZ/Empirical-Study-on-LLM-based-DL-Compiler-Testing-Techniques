import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(10, 10)
_output_tensor = torch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)