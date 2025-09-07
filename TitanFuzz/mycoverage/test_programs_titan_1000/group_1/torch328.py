import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
other = torch.tensor([2], dtype=torch.int32)
output = torch.Tensor.bitwise_right_shift_(input_tensor, other)