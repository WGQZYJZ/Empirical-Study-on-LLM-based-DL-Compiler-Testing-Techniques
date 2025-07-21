'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
import torch.nn.functional as F
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5))
output = F.adaptive_max_pool2d(input, (2, 2))
print(output)
print(output.shape)