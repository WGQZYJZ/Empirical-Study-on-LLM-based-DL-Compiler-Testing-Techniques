import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([2, 3, 4, 5, 6])
torch.lcm(input_data, input_data)