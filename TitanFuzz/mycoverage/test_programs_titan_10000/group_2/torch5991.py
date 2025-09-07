import torch
from torch import nn
from torch.autograd import Variable

tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
result = torch.addcmul(tensor1, tensor2, tensor1)