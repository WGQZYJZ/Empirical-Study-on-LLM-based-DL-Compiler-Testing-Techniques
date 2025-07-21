'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(20, 16, 50))
pooling_L1 = torch.nn.LPPool1d(1, kernel_size=2, stride=2, ceil_mode=False)
output = pooling_L1(input_data)
print(output.size())