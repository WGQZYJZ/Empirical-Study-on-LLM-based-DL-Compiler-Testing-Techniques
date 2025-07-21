import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randint(10, (3, 3), dtype=torch.float)
result_data = torch.fmod(input_data, 2)