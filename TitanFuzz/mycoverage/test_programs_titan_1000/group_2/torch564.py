import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
torch.set_default_tensor_type(torch.DoubleTensor)
y = torch.rand(5, 3)