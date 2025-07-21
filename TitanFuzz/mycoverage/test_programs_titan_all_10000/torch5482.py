import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1024, 1024)
y = torch.randn(1024, 1024)
torch.get_num_threads()
torch.set_num_threads(1)
torch.get_num_threads()
torch.set_num_threads(4)
torch.get_num_threads()