import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(20, 16, 50, 32)
output = torch.empty_strided(size=(20, 16, 50, 32), stride=(1, 1, 1, 1))