'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 4, 4))
print('Input size: ', input.size())
pad = torch.nn.ReplicationPad2d(2)
output = pad(input)
print('Output size: ', output.size())
print('Output: ', output)