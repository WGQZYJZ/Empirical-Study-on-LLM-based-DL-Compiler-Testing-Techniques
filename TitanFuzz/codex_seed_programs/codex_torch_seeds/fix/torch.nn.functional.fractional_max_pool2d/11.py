'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(1, 2, 5, 5)
output = F.fractional_max_pool2d(input_data, kernel_size=(2, 2), output_size=(2, 2))
print(output)