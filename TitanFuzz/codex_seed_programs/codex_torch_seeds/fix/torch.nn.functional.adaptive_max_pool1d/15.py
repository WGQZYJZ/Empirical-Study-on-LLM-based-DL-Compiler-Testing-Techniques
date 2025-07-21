'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input = Variable(torch.randn(1, 3, 10))
F.adaptive_max_pool1d(input, 5, return_indices=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input = Variable(torch.randn(1, 3, 10, 10))
F.adaptive_max_pool2d(input, 5, return_indices=False)