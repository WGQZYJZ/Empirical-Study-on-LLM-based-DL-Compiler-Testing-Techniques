import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.rand(1000000)
torch.set_num_threads(1)
result = torch.sum(input_data)