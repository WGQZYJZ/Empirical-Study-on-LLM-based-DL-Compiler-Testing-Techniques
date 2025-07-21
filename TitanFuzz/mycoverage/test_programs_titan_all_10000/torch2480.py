import torch
from torch import nn
from torch.autograd import Variable
batch_size = 3
input_size = 5
hidden_size = 4
batch1 = torch.randn(batch_size, input_size, hidden_size)
batch2 = torch.randn(batch_size, hidden_size, input_size)
output = torch.Tensor.addbmm(batch1, batch2)