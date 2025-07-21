import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
tensor1 = torch.randn(4, 4)
tensor2 = torch.randn(4, 4)
tensor3 = torch.Tensor.addcdiv_(input_tensor, tensor1, tensor2, value=1)