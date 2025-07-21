import torch
from torch import nn
from torch.autograd import Variable
tensor_1 = torch.rand(2, 2)
tensor_2 = torch.rand(2, 2)
tensor_3 = torch.rand(2, 2)
result = torch.dstack((tensor_1, tensor_2, tensor_3))