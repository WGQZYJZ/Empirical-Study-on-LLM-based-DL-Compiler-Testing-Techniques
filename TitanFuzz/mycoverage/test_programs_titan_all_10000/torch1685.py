import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(size=(3, 3), dtype=torch.float32)
torch.Tensor.set_(_input_tensor, source=None, storage_offset=0, size=None, stride=None)