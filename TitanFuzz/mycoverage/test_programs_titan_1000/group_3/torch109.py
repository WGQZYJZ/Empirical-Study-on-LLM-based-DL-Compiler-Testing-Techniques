import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
output = torch.addcmul(input, tensor1, tensor2)