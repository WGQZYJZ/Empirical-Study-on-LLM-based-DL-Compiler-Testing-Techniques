'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
torch.nn.init.orthogonal_(input_data)
print(input_data)
torch.nn.init.orthogonal_(input_data, gain=2)
print(input_data)