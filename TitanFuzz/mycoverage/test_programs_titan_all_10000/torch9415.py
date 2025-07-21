import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 3, 3)
torch.set_default_tensor_type(torch.DoubleTensor)
torch.set_default_dtype(torch.float32)