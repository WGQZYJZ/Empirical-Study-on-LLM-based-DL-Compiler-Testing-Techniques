import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([float('-inf'), float('inf'), float('nan'), float('inf'), float('-inf')])
torch.Tensor.isneginf(input_tensor)