import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
torch.Tensor.apply_(input_tensor, (lambda x: (x * 2)))
input_tensor = torch.randn(4, 4)
input_tensor.apply_((lambda x: (x * 2)))