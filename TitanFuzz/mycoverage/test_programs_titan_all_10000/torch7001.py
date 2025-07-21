import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.arange(0, 10)
torch.Tensor.storage_type(_input_tensor)