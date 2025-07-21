import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 224, 224)
torch.Tensor.as_subclass(input_tensor, nn.Module)