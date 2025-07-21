'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
import torch
input_data = torch.randn(1, 1, 5, 7)
output = F.fractional_max_pool2d(input_data, kernel_size=(2, 3), output_size=(1, 2))
print(output)