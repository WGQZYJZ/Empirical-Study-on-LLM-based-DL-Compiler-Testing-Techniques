'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 5, 5, 5, requires_grad=True)
output = F.fractional_max_pool3d(input, kernel_size=(3, 3, 3), output_size=(1, 1, 1))
print(output)