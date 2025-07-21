import torch
from torch import nn
from torch.autograd import Variable
indices = torch.LongTensor([[0, 1, 1], [2, 0, 2]])
values = torch.FloatTensor([3, 4, 5])
size = torch.Size([3, 3])
result = torch.sparse_coo_tensor(indices, values, size)