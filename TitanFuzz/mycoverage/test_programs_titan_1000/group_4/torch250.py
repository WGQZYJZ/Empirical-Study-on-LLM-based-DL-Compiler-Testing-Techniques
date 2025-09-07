import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(1, 10, (4, 4))
torch.Tensor.fmod_(input_tensor, 3)