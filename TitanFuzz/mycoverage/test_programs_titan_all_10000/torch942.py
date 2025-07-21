import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor(2, 3))
torch.nn.init.xavier_uniform_(input_data)