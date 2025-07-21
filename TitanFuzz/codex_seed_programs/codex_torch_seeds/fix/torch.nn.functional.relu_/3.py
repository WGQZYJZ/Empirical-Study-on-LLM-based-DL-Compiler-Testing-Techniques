'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(2, 3))
print('input: ', input)
output = torch.nn.functional.relu_(input)
print('output: ', output)