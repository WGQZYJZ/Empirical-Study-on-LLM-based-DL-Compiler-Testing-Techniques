import torch
from torch import nn
from torch.autograd import Variable
i = torch.tensor([[0, 1, 1], [2, 0, 2]])
v = torch.tensor([3, 4, 5], dtype=torch.float32)
shape = torch.Size([3, 3])
mat1 = torch.sparse_coo_tensor(i, v, shape)
i = torch.tensor([[0, 1, 1], [2, 0, 2]])
v = torch.tensor([1, 2, 3], dtype=torch.float32)
shape = torch.Size([3, 3])
mat2 = torch.sparse_coo_tensor(i, v, shape)
result = torch.sparse.mm(mat1, mat2)