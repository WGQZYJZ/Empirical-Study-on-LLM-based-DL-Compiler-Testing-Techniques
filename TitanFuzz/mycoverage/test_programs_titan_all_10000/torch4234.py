import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
torch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)