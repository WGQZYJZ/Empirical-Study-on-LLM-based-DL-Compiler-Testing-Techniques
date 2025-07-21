'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(4, 4))
output = torch.nn.functional.hardswish(input)
print(output)