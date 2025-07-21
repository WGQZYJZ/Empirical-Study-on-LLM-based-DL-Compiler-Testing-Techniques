import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(10, (3, 3), dtype=torch.float64)
input_data = torch.randint(10, (3, 3), dtype=torch.float64)
output = torch.remainder(input_data, 2)