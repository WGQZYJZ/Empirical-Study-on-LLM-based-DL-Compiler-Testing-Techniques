'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5))
print(input)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=1)
print(output)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=2)
print(output)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=3)
print(output)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=4)
print(output)
output = torch.nn.functional.adaptive_max_pool1d(input, output_size=5)
print(output)