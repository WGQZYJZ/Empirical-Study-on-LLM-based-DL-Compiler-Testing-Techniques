import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 17, dtype=torch.float32).view(1, 1, 4, 4)
pool = torch.nn.LPPool2d(2, 3, stride=2)
output = pool(input_data)