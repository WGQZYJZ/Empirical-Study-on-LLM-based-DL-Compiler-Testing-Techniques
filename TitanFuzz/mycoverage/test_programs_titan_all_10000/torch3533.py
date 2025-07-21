import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 3)
index_data = torch.tensor([1, 2])
output_data = torch.index_select(input_data, dim=0, index=index_data)