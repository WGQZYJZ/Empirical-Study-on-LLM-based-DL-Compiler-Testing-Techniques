import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 6)
narrow_copy_tensor = torch.Tensor.narrow_copy(input_tensor, 1, 2, 3)