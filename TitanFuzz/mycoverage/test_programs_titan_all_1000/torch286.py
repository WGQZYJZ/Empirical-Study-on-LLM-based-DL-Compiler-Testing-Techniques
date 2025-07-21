import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.randn(5, 5)
tensor2 = torch.randn(5, 5)
torch.Tensor.addcmul(tensor1, tensor2, tensor2, value=1)