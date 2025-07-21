import torch
from torch import nn
from torch.autograd import Variable
vec1 = torch.tensor([1, 2, 3], dtype=torch.float32)
vec2 = torch.tensor([4, 5, 6], dtype=torch.float32)
output = torch.Tensor.addr_(vec1, vec2, beta=1, alpha=1)