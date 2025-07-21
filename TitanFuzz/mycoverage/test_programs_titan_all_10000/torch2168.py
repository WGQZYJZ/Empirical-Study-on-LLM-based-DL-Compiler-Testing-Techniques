import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)