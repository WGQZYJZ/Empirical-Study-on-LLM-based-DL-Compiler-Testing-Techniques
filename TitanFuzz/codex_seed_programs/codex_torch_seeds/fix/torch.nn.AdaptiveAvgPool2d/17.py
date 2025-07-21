'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 32, 32))
output = torch.nn.AdaptiveAvgPool2d(output_size=(4, 4))(input)
print(output.size())