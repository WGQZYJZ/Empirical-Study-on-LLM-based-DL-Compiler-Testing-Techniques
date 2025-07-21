import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(3, 3)
corr_matrix = torch.corrcoef(input_data)