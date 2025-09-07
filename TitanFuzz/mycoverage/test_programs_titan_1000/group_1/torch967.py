import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=2)