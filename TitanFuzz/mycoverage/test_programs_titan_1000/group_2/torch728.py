import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 2, 2)
torch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)