import torch
from torch import nn
from torch.autograd import Variable
tensor_a = torch.randn(4, 3)
tensor_b = torch.randn(4, 1)
tensor_c = torch.randn(3, 4)
torch.Tensor.addr_(tensor_a, tensor_b, tensor_c)
tensor_a = torch.randn(4, 3)
tensor_b = torch.randn(4, 1)
tensor_c = torch.randn(3, 4)
torch.Tensor.addr_(tensor_a, tensor_b, tensor_c, beta=0.5, alpha=0.5)