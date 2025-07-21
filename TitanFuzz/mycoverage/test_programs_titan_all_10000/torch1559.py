import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(5)
output = torch.bartlett_window(5)