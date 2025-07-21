import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)