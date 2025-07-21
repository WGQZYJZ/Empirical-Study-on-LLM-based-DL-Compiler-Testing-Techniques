import torch
from torch import nn
from torch.autograd import Variable
input_data1 = torch.randn(5, 3)
input_data2 = torch.randn(5, 3)
dataset = torch.utils.data.ConcatDataset([input_data1, input_data2])
input_data1 = torch.randn(5, 3)
input_data2 = torch.randn(5, 3)
dataset = torch.utils.data.TensorDataset(input_data1, input_data2)