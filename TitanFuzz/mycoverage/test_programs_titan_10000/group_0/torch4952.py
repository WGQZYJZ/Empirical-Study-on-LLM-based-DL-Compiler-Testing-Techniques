import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(2, 3)
subclass_tensor = torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)