'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
x = torch.randn(1, 1, 5, 5)
print(x)
print(F.fractional_max_pool2d(x, kernel_size=3, output_size=3))