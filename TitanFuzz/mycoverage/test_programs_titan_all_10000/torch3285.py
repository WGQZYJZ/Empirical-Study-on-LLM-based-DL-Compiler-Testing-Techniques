import torch
from torch import nn
from torch.autograd import Variable
indices = torch.tensor([[1, 0, 2], [0, 2, 1]])
values = torch.tensor([1, 2, 3])
torch.sparse_coo_tensor(indices, values, size=(3, 3))