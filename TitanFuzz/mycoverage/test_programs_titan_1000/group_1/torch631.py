import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index_data = torch.tensor([0, 2])
output_data = torch.index_select(input_data, dim=0, index=index_data)
output_data = torch.index_select(input_data, dim=1, index=index_data)