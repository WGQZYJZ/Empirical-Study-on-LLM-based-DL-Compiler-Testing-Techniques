'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 5))
pool = torch.nn.functional.adaptive_max_pool1d(x, output_size=3)
print(pool)