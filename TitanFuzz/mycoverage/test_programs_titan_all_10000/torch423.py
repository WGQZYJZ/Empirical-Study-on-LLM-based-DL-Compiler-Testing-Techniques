import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
torch.Tensor.normal_(input_data, mean=0, std=1)
torch.Tensor.normal_(input_data, mean=0, std=1, generator=None)
torch.Tensor.normal_(input_data, mean=torch.randn(2, 3), std=torch.randn(2, 3))