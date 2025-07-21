import torch
from torch import nn
from torch.autograd import Variable
data_size = 5
data_low = 0
data_high = 10
output = torch.randint(low=data_low, high=data_high, size=(data_size,), dtype=torch.float32)