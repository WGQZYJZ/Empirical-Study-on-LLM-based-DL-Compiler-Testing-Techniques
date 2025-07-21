import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
result = torch.tril(input_data, diagonal=1)
result = torch.tril(input_data, diagonal=0)
result = torch.tril(input_data, diagonal=2)