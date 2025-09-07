import torch
from torch import nn
from torch.autograd import Variable
vec1 = torch.tensor([1, 2, 3, 4, 5])
vec2 = torch.tensor([5, 4, 3, 2, 1])
vec1 = torch.tensor([1, 2, 3, 4, 5])
vec2 = torch.tensor([5, 4, 3, 2, 1])
torch.Tensor.outer(vec1, vec2)
mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]])