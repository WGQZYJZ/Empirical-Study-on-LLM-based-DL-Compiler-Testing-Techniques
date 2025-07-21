import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor(1, 1, 3, 3))
torch.nn.init.zeros_(input_data)
torch.nn.init.ones_(input_data)
torch.nn.init.normal_(input_data)
torch.nn.init.uniform_(input_data)