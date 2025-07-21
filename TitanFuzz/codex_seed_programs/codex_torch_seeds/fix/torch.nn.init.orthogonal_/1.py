'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
from torch.autograd import Variable
input_size = 2
output_size = 3
input_data = Variable(torch.randn(input_size, output_size))
print('Input data:')
print(input_data)
torch.nn.init.orthogonal_(input_data)
print('Output data:')
print(input_data)