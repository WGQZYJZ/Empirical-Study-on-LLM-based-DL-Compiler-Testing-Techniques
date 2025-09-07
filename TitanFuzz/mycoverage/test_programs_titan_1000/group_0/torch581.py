import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.int32)
torch.Tensor.mul_(input_tensor, 2)