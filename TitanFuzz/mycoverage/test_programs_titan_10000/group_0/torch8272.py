import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(5, 5)
torch.set_num_threads(8)