import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1.0), 1.0, 2.0])
relu = torch.nn.ReLU()
output = relu(input_data)
relu = torch.nn.ReLU(inplace=True)
output = relu(input_data)