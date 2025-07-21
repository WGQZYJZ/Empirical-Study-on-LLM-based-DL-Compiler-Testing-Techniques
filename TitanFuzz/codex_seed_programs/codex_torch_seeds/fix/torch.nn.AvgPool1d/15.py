'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]))
avgpool1d = torch.nn.AvgPool1d(kernel_size=2, stride=2)
output = avgpool1d(input)
print(output)