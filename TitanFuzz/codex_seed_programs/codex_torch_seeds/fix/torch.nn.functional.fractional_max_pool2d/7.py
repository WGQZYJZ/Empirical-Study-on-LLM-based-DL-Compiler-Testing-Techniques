'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
input_tensor = torch.rand(1, 2, 3, 3)
print('Input tensor: ', input_tensor)
output_tensor = F.fractional_max_pool2d(input_tensor, kernel_size=[2, 2], output_size=[2, 2])
print('Output tensor: ', output_tensor)