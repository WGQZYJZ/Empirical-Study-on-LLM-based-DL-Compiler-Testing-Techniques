import torch
from torch import nn
from torch.autograd import Variable
values = torch.tensor([1, 2, 3, 4, 5, 6], dtype=torch.float32)
indices = torch.tensor([[0, 1, 1, 2, 2, 3], [0, 0, 1, 0, 1, 2]], dtype=torch.int64)
size = torch.Size([4, 3])
output = torch.sparse_coo_tensor(indices, values, size)