"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Conv2d\ntorch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 28, 28))
conv1 = torch.nn.Conv2d(1, 1, 3, 1, 1)
output = conv1(input)
print(input.size())
print(output.size())
pool1 = torch.nn.MaxPool2d(2, 2)
output = pool1(output)
print(output.size())
relu1 = torch.nn.ReLU()
output = relu1(output)
print(output.size())