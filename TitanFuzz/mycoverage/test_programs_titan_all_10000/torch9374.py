import torch
from torch import nn
from torch.autograd import Variable
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = torch.Tensor(data)
result = torch.block_diag(data, data, data)