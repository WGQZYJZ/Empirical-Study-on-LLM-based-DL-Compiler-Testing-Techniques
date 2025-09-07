import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10)
torch.get_num_threads()
torch.set_num_threads(2)
torch.get_num_threads()