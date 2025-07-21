import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.apply_(input_tensor, (lambda x: (x * 2)))