import torch
from torch import nn
from torch.autograd import Variable
tensor_a = torch.randn(3, 3)
tensor_b = torch.randn(3, 3)
result = torch.sub(tensor_a, tensor_b)