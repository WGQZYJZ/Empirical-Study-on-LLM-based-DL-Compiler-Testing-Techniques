import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
torch.Tensor.index_fill_(input_tensor, dim=1, index=torch.tensor([0, 2]), value=0)