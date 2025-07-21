'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool3d\ntorch.nn.AvgPool3d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 5, 5, 5))
avgpool3d = torch.nn.AvgPool3d(kernel_size=3, stride=2, padding=1)
output = avgpool3d(input_data)
print(output)