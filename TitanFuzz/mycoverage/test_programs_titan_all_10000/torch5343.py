import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 5)
torch.set_default_tensor_type(torch.FloatTensor)