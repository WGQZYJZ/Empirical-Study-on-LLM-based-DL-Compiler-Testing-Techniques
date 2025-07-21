import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.FloatTensor([[2, 3], [4, 5]])
other_data = torch.FloatTensor([[1, 2], [3, 4]])
divide_result = torch.divide(input_data, other_data)