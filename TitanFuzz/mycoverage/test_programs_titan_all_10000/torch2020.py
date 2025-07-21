import torch
from torch import nn
from torch.autograd import Variable
indices = torch.LongTensor([[0, 1, 1], [2, 0, 2]])
values = torch.FloatTensor([3, 4, 5])
shape = torch.Size([3, 3])
sparse_matrix = torch.sparse.FloatTensor(indices, values, shape)
dense_matrix = torch.FloatTensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = torch.sparse.mm(sparse_matrix, dense_matrix)
indices = torch.LongTensor([[0, 1, 1], [2, 0, 2]])
values