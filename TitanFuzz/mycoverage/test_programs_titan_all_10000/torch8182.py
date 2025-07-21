import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
tensor2 = torch.randn(5, 4)
result = torch.Tensor.matmul(input_tensor, tensor2)