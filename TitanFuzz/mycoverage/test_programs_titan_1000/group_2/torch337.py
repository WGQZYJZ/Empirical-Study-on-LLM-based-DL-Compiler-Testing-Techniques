import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(1, 3, 224, 224)
torch.Tensor.isreal(_input_tensor)