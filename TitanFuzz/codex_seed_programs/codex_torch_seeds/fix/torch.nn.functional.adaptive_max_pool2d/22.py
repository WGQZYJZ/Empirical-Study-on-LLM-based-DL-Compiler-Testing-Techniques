'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(1, 1, 3, 3))
torch.nn.functional.adaptive_max_pool2d(input, (2, 2))
input = Variable(torch.randn(1, 1, 3, 3))
torch.nn.functional.adaptive_max_pool2d(input, (2, 2), return_indices=True)
input = Variable(torch.randn(1, 1, 3, 3))