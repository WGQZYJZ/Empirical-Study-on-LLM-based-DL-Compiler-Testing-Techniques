import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (3, 3))
mask = torch.tensor([[True, False, False], [False, True, True], [True, False, True]])
source = torch.tensor([1, 2, 3])
torch.Tensor.masked_scatter_(input_tensor, mask, source)