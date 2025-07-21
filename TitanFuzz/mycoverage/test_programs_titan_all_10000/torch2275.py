import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)