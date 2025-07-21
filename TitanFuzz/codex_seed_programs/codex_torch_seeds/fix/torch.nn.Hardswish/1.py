'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(5, 3))
hardswish = torch.nn.Hardswish(inplace=False)
print('The input size is: ', input_data.size())
print('The output size is: ', hardswish(input_data).size())
print('The learnable parameters are: ', list(hardswish.parameters()))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch