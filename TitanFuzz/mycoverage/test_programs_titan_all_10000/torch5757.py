import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 3, 3)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=False)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.01, inplace=True)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.5, inplace=False)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.5, inplace=True)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.99, inplace=False)
torch.nn.functional.leaky_relu(input_data, negative_slope=0.99, inplace=True)