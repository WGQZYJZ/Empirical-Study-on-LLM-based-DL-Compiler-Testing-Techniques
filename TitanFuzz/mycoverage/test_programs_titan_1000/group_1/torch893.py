import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([0.2, 0.3, 0.4])
torch.Tensor.geometric_(input_tensor, p=0.5)