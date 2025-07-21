'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
from torch.autograd import Function
import torch.nn.functional as F
import torch
input_data = torch.randn(1, 1, 12, 12, 12)
output = F.fractional_max_pool3d(input_data, kernel_size=[3, 3, 3], output_size=[3, 3, 3])
print(output)