'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
import torch
input_data = torch.randn(1, 3, 8, 8, 8)
output = torch.nn.functional.fractional_max_pool3d(input_data, kernel_size=(3, 3, 3), output_size=(3, 3, 3))
print(output)
'\ntorch.Size([1, 3, 3, 3, 3])\n'