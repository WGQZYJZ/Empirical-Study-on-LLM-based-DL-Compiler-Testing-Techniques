import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(1, 2, 3, 4))
torch.Tensor.int_repr(input_tensor)