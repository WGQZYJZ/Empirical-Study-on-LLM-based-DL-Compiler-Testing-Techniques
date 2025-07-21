import torch
from torch import nn
from torch.autograd import Variable
tensor_data = torch.arange(0, 20)
tensor_data_split = torch.hsplit(tensor_data, 5)
tensor_data_split = torch.hsplit(tensor_data, [3, 4, 6, 10])