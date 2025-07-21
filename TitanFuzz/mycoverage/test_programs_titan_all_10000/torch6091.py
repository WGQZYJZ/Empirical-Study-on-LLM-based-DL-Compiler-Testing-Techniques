import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 11, dtype=torch.float32).view(1, 1, 10)
output = torch.nn.functional.pad(input_data, [2, 3], mode='constant', value=0)