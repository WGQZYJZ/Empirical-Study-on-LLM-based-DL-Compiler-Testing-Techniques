import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(10, (2, 3))
other = torch.randint(10, (2, 3))
result = torch.Tensor.not_equal(input_tensor, other)