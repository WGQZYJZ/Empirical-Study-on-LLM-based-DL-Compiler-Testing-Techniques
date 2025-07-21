import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
torch.Tensor.index_fill_(input_tensor, 0, torch.LongTensor([0, 1]), 1)
torch.Tensor.index_fill_(input_tensor, 1, torch.LongTensor([0, 1]), 1)