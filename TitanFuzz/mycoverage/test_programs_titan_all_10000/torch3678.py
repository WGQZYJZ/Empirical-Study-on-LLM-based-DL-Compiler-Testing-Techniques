import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5, dtype=torch.float)
tensor1 = torch.randn(5, 5, dtype=torch.float)
tensor2 = torch.randn(5, 5, dtype=torch.float)
torch.Tensor.addcmul(input_tensor, tensor1, tensor2)