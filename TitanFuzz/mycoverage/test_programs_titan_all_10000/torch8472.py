import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(low=0, high=10, size=(4, 4))
result = torch.randint(low=0, high=10, size=(4, 4))