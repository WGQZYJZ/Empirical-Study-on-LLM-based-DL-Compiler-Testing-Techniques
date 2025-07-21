import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3)
norm_1 = torch.norm(input_data, p=1)
norm_2 = torch.norm(input_data, p=2)
norm_3 = torch.norm(input_data, p=3)
norm_inf = torch.norm(input_data, p=float('inf'))