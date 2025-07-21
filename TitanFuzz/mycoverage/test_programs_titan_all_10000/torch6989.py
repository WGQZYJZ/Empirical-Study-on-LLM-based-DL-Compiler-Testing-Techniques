import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 5)
torch.Tensor.set_(input_tensor, source=None, storage_offset=0, size=None, stride=None)