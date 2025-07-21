import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.FloatTensor(3, 3)
torch.nn.init.ones_(input_tensor)