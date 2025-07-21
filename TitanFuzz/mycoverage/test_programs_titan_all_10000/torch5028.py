import torch
from torch import nn
from torch.autograd import Variable
input_data_1 = torch.rand(5, 3)
input_data_2 = torch.rand(5, 3)
input_data_3 = torch.rand(5, 3)
dataset = torch.utils.data.ConcatDataset([input_data_1, input_data_2, input_data_3])