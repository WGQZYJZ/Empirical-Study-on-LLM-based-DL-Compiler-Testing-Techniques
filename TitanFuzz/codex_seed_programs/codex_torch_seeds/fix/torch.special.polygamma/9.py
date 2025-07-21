'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 3))
print('Input data: ', input_data)
output = torch.special.polygamma(1, input_data)
print('Output: ', output)