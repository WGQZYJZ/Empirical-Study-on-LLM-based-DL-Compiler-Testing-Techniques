'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(5), requires_grad=True)
output = torch.nn.LogSoftmax(input)
print(output)