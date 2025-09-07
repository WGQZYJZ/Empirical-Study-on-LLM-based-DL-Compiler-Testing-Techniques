import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 3)
torch.hub.help(github='pytorch/vision:v0.3.0', model='alexnet', force_reload=False, skip_validation=False)