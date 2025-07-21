import torch
from torch import nn
from torch.autograd import Variable
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
size = torch.Size([3, 3])
input = torch.sparse_coo_tensor(indices, values, size)
output = torch.sparse.sum(input, dim=None, dtype=None)