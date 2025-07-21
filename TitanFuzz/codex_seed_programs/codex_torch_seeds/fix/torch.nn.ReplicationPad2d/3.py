'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
padding = 1
output = torch.nn.ReplicationPad2d(padding)(input)
print('input: ', input)
print('output: ', output)