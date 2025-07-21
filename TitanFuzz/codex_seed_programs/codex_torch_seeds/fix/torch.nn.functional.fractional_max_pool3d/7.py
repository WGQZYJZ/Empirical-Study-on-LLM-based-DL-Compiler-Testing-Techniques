'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
input_data = torch.randn(1, 1, 4, 4, 4)
torch.nn.functional.fractional_max_pool3d(input_data, kernel_size=[2, 2, 2], output_size=[2, 2, 2])