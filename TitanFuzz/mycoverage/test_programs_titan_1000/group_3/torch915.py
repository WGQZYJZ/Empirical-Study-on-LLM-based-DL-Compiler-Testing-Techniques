import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (10,))
result = torch.Tensor.bincount(input_tensor, minlength=10)