import torch
from torch import nn
from torch.autograd import Variable
input_data_1 = torch.rand(2, 3)
input_data_2 = torch.rand(2, 3)
torch.hstack((input_data_1, input_data_2))
torch.vstack((input_data_1, input_data_2))
torch.stack((input_data_1, input_data_2))
torch.cat((input_data_1, input_data_2), dim=0)
torch.cat((input_data_1, input_data_2), dim=1)
torch.chunk(input_data_1, 2, dim=0)
torch.chunk(input_data_1, 3, dim=1)