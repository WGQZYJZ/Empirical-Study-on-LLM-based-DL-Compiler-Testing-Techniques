import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
index = torch.tensor([0, 2], dtype=torch.int64)
output = torch.index_select(input, 1, index)