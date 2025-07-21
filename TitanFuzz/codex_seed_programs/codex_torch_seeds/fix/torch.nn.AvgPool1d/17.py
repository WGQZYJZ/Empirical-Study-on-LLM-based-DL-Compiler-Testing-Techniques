'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[1, 2, 3, 4, 5, 6, 7]]))
print('input_data: ', input_data)
avg_pooling = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0)
output = avg_pooling(input_data)
print('output: ', output)