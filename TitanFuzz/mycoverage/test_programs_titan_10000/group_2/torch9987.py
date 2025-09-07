import torch
from torch import nn
from torch.autograd import Variable

a = torch.rand(2, 3)
torch.set_default_tensor_type(torch.FloatTensor)
b = torch.rand(2, 3)
torch.set_default_tensor_type(torch.DoubleTensor)
c = torch.rand(2, 3)