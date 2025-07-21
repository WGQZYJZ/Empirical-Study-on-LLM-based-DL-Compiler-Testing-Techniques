import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 5)
torch.initial_seed()
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.enabled = False