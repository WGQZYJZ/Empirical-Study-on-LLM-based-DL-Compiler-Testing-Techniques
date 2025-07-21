'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5))
output = torch.nn.AdaptiveAvgPool1d(4)(input)
print(output)