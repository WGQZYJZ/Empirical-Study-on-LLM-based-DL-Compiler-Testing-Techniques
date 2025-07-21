'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor(2, 3))
torch.nn.init.xavier_uniform_(input_data)
print(input_data)