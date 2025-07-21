'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(4, 4))
print('Input:\n', input)
relu6 = torch.nn.ReLU6()
output = relu6(input)
print('Output:\n', output)