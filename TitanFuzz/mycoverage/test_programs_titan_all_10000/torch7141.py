import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(4, 4)
torch.set_default_tensor_type(torch.DoubleTensor)