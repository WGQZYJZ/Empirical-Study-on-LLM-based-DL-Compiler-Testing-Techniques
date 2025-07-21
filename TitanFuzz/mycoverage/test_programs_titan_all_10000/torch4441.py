import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(1, 3, 224, 224)
torch.Tensor.data_ptr(_input_tensor)