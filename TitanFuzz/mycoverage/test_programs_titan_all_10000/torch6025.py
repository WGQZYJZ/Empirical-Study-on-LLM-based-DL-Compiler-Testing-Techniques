import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
true_divide_result = torch.Tensor.true_divide_(input_tensor, 2)
true_divide_result = torch.true_divide(input_tensor, 2)