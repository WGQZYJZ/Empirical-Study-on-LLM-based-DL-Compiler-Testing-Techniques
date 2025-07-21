import torch
from torch import nn
from torch.autograd import Variable
data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.int32)
other = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.int32)
torch.Tensor.gcd_(data, other)