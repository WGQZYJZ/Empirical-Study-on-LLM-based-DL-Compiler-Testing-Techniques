import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.matmul(input_tensor, torch.randn(3, 4))