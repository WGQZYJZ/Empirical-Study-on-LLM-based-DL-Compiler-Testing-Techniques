import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
tensor1 = torch.randn(4, 4)
tensor2 = torch.randn(4, 4)
output = torch.addcmul(input, tensor1, tensor2)