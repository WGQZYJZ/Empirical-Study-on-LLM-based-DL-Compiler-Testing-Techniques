import torch
from torch import nn
from torch.autograd import Variable
tensor_1 = torch.arange(1, 11)
tensor_2 = torch.Tensor.as_strided(tensor_1, (4, 3), (2, 2))