import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[2, 3, 4], [5, 6, 7]], dtype=torch.float32)
other = torch.tensor([[2, 3, 4], [5, 6, 7]], dtype=torch.float32)
result = torch.le(input, other)