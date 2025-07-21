import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, requires_grad=True)
tensor1 = torch.ones(3, 3, dtype=torch.float32)
tensor2 = torch.ones(3, 3, dtype=torch.float32)
output = torch.addcdiv(input, tensor1, tensor2)