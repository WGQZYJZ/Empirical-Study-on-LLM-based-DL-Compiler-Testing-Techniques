import torch
from torch import nn
from torch.autograd import Variable
vec1 = torch.tensor([1, 2, 3, 4, 5, 6])
vec2 = torch.tensor([1, 2, 3, 4, 5, 6])
torch.Tensor.addr_(vec1, vec2)
vec1 = torch.tensor([1, 2, 3, 4, 5, 6])
vec2 = torch.tensor([1, 2, 3, 4, 5, 6])
torch.Tensor.addr_(vec1, vec2)