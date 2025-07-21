import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.ones([3, 3], dtype=torch.int8)
torch.Tensor.int_repr(_input_tensor)
_input_tensor = torch.ones([3, 3], dtype=torch.float32)
torch.Tensor.is_floating_point(_input_tensor)