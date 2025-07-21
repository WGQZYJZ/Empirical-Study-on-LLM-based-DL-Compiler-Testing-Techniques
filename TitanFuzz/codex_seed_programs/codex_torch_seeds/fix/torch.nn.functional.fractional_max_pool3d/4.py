'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
from torch.nn.functional import fractional_max_pool3d
input_data = torch.arange(1, 65).view(1, 1, 4, 4, 4).float()
output = fractional_max_pool3d(input_data, kernel_size=(2, 2, 2), output_size=(2, 2, 2))
print(output)