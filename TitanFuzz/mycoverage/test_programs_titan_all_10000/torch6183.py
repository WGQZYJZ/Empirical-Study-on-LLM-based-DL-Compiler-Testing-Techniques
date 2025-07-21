import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
target = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
loss = torch.nn.L1Loss()
output = loss(input, target)