import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(0, 10, (3, 3), dtype=torch.float32)
output = torch.floor_divide(input_data, 2)