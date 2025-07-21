'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
input_data = Variable(torch.randn(10, 5))
torch.nn.init.xavier_uniform_(input_data)
print(input_data)
input_data = Variable(torch.randn(10, 5))
torch.nn.init.xavier_normal_(input_data)
print(input_data)