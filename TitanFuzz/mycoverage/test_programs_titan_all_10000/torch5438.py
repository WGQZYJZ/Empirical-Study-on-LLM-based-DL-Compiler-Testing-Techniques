import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor(2, 3)
torch.nn.init.normal_(input_data)