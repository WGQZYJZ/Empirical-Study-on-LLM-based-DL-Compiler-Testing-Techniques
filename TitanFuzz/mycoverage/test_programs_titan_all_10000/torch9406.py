import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 5)
index = torch.tensor([0, 2])
source = torch.randn(2, 5)
torch.Tensor.index_copy_(input_tensor, dim=0, index=index, source=source)