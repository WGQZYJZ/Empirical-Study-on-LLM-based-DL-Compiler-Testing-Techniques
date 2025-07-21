'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
from torch.nn import functional as F
import torch
input_data = torch.rand(2, 3, 8, 8)
result = F.fractional_max_pool2d(input_data, kernel_size=(2, 2), output_size=(4, 4))
print(result)