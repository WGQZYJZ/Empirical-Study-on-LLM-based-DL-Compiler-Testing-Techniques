'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input = Variable(torch.randn(1, 2, 10, 10, 10))
output = F.fractional_max_pool3d(input, kernel_size=(1, 2, 2), output_size=(2, 3, 3))
print(output)