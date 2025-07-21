'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
pool = torch.nn.AdaptiveMaxPool2d(output_size=(2, 2))
output = pool(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
pool = torch.nn.AdaptiveAvgPool2d(output_size=(2, 2))
output = pool(input)
print(output)