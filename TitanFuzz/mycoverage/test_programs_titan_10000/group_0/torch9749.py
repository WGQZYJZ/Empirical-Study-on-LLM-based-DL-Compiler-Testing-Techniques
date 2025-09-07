import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([(- 1.0), 1.0, 2.0, 3.0])
output_data = torch.nn.Tanh()(input_data)