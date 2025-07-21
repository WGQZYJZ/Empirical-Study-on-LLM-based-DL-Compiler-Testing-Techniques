import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4, dtype=torch.float32)
_half_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)
_half_tensor = torch.Tensor.half(_input_tensor, memory_format=torch.channels_last)