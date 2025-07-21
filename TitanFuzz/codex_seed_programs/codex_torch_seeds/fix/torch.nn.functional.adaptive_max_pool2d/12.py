'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool2d\ntorch.nn.functional.adaptive_max_pool2d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 4, 4))
output = torch.nn.functional.adaptive_max_pool2d(input_data, (1, 1))
print(output)