import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 2, size=(2, 3))
torch.Tensor.bitwise_left_shift_(input_tensor, 2)