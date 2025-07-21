import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 5)
torch.Tensor.share_memory_(input_tensor)