import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.ones(3, 3)
index = torch.tensor([[0, 1], [1, 2]])
source = torch.tensor([3, 4])
torch.Tensor.put_(input_tensor, index, source, accumulate=False)