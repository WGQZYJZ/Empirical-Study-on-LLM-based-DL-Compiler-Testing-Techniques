import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (3, 3))
mask = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.uint8)
value = torch.tensor(1)
torch.Tensor.masked_fill_(input_tensor, mask, value)