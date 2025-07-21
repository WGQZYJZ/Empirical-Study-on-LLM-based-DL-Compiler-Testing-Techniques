'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
output = torch.nn.LogSoftmax(dim=1)(input_data)
print(output)