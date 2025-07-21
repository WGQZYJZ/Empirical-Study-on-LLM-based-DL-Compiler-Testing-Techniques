'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import adaptive_avg_pool2d
import torch
input = Variable(torch.randn(1, 1, 4, 4))
output = adaptive_avg_pool2d(input, (1, 1))
print(output)