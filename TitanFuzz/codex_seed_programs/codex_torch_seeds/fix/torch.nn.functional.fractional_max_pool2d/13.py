'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
output = F.fractional_max_pool2d(input, kernel_size=2, output_size=(3, 3))
print(output)
print(output.shape)