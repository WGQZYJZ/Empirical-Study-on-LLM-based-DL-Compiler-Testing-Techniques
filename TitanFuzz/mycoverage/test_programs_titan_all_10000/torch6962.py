import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10, device='cpu')
torch.get_num_threads()