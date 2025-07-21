import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 3, 28, 28)
norm_result = torch.Tensor.norm(input_tensor)