'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
from torch.autograd import Variable
import torch
input = torch.randn(1, 1, 4)
print(input)
avg_pool = torch.nn.AdaptiveAvgPool1d(1)
output = avg_pool(Variable(input))
print(output)