import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3)
torch.Tensor.type_as(_input_tensor, torch.FloatTensor)