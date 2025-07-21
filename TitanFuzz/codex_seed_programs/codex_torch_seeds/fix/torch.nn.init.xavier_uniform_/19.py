'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(5, 3))
torch.nn.init.xavier_uniform_(input_data)
print(input_data)
torch.nn.init.xavier_uniform_(input_data, gain=0.5)
print(input_data)