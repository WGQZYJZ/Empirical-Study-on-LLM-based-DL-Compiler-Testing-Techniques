'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 5))
print(input_data)
avg_pool1d = torch.nn.AvgPool1d(kernel_size=2, stride=2)
output = avg_pool1d(input_data)
print(output)