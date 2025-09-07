import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
other_data = torch.randn(10)
torch.minimum(input_data, other_data)
torch.minimum(torch.arange(1, 6), torch.arange(3, 8))
torch.minimum(torch.arange(1, 6), torch.arange(3, 8)).dtype
torch.minimum(torch.arange(1, 6, dtype=torch.int64), torch.arange(3, 8, dtype=torch.int64))