import torch
from torch import nn
from torch.autograd import Variable
tensor_1 = torch.randn(3, 2)
tensor_2 = torch.randn(3, 2)
tensor_3 = torch.row_stack((tensor_1, tensor_2))