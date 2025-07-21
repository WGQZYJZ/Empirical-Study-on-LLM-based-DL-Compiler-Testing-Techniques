import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.randn(2, 3, requires_grad=True)
tensor2 = torch.randn(2, 3, requires_grad=True)
tensor3 = torch.randn(2, 3, requires_grad=True)
result = torch.Tensor.addcdiv(tensor1, tensor2, tensor3, value=1)
tensor1 = torch.randn(2, 3, requires_grad=True)
tensor2 = torch.randn(2, 3, requires_grad=True)
tensor3 = torch.randn(2, 3, requires_grad=True)
result = torch.Tensor.add