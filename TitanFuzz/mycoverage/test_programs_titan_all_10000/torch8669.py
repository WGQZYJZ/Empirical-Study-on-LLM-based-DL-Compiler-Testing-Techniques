import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100, 100)
relu_output = torch.nn.functional.relu(input_data)