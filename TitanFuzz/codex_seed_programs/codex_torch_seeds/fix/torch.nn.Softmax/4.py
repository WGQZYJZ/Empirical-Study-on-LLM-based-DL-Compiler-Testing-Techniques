'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
softmax_output = torch.nn.Softmax(dim=1)(input_data)
print(softmax_output)
print(softmax_output.sum(dim=1))