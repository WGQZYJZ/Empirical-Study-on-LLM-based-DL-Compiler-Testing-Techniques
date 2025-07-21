import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.ones([2, 2])
output_tensor = torch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)