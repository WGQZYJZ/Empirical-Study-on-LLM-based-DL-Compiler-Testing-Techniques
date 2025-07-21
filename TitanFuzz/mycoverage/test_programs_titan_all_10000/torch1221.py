import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (3, 3))
mask = torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=torch.bool)
value = torch.tensor(100)
result = torch.Tensor.masked_fill_(input_tensor, mask, value)