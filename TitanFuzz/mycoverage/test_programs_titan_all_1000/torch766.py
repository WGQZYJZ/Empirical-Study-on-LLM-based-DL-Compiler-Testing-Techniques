import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)