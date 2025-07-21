import torch
from torch import nn
from torch.autograd import Variable
data1 = torch.rand(2, 3, 4)
data2 = torch.rand(2, 3, 4)
data3 = torch.rand(2, 3, 4)
result = torch.addcmul(data1, data2, data3, value=0.5)