import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[7, 8], [9, 10], [11, 12]], dtype=torch.float32)
result = torch.einsum('ij,jk->ik', x, y)