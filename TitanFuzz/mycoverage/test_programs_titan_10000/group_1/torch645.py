import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.Tensor([(- 1), 0, 1])
frexp_output = torch.Tensor.frexp(input_tensor)