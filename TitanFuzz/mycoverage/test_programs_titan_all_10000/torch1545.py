import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(10, 3, 4)
batch2 = torch.rand(10, 4, 5)
torch.Tensor.bmm(_input_tensor, batch2)
_input_tensor = torch.rand(10, 3, 4)
chunks = 3
dim = 1
torch.Tensor.chunk(_input_tensor, chunks, dim)