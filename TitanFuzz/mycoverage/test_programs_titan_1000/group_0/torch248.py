import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (2, 3))
other = torch.randint(0, 10, (2, 3))
result = torch.Tensor.minimum(input_tensor, other)