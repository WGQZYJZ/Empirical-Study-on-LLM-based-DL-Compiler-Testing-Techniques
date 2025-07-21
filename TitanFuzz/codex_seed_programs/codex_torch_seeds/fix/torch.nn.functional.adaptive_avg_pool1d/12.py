'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 64, 8))
output = torch.nn.functional.adaptive_avg_pool1d(input, (1,))
print(output.size())