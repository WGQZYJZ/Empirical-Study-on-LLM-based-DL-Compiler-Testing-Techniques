import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 1, 1, 1)
torch.Tensor.is_quantized(_input_tensor)