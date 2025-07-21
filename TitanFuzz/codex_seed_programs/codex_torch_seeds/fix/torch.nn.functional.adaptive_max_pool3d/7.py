'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(1, 3, 10, 10, 10))
output = torch.nn.functional.adaptive_max_pool3d(input_tensor, (1, 1, 1))
print(output.size())
output = torch.nn.functional.adaptive_max_pool3d(input_tensor, (2, 2, 2))
print(output.size())
output = torch.nn.functional.adaptive_max_pool3d(input_tensor, (4, 4, 4))
print(output.size())