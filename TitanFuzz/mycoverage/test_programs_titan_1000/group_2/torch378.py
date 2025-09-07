import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
index_tensor = torch.tensor([0, 1, 2, 0, 2, 1])
source_tensor = torch.randn(6, 3)
torch.Tensor.index_copy_(input_tensor, dim=0, index=index_tensor, source=source_tensor)