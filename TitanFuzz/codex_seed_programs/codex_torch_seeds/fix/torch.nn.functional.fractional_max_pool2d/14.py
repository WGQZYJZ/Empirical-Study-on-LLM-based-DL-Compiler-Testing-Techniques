'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input = Variable(torch.randn(1, 1, 10, 10))
output = F.fractional_max_pool2d(input, kernel_size=3, output_size=(3, 3))
print(output)
print(output.size())