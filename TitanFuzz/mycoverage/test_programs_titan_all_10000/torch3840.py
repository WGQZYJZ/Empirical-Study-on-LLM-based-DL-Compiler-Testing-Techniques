import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4)
torch.Tensor.is_contiguous(_input_tensor, memory_format=torch.contiguous_format)