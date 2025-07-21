import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
tensor1 = torch.randn(3, 4, 5)
tensor2 = torch.randn(3, 4, 5)
out = torch.addcmul(input, tensor1, tensor2)