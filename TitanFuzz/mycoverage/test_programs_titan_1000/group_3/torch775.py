import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.ones(3, 3)
bartlett_window = torch.bartlett_window(3)