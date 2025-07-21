import torch
from torch import nn
from torch.autograd import Variable
indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
x = torch.sparse_coo_tensor(indices, values, size=(3, 3))
x = torch.sparse_coo_tensor(indices, values, size=(3, 3), dtype=torch.float64)
indices = torch.tensor([[0, 1, 1], [2, 0, 2]], dtype=torch.long)
values = torch.tensor([3, 4, 5], dtype=torch.float32)