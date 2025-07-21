import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
output_tensor = torch.Tensor.tanh_(input_tensor)