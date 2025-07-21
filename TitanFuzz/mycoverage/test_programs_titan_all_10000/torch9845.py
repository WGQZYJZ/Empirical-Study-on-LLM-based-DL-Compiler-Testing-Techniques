import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.int16)
torch.Tensor.bitwise_right_shift_(input_tensor, other=2)