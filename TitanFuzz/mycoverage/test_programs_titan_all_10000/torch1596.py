import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 5)
torch.nn.init.xavier_uniform_(input_tensor)