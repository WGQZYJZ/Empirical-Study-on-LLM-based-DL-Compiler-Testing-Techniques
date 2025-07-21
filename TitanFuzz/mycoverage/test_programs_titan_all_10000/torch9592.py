import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
input_data = torch.randn(2, 3)
torch.Tensor.copy_(input_tensor, input_data, non_blocking=False)