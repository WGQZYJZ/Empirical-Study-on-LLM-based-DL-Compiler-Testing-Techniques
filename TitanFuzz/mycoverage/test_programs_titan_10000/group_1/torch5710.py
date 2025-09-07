import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(5, 3)
y = torch.rand(5, 3)
torch.set_num_threads(2)
z = torch.add(x, y)