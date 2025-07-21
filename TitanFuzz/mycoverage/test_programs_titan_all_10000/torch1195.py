import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 224, 224)
torch.Generator(device='cpu')