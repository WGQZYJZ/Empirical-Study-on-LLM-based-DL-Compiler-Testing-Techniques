import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
k = 1
(values, indices) = torch.kthvalue(input_data, k)