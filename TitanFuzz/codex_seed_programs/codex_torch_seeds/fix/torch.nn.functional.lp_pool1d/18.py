'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
input_data = torch.arange(1, 9, dtype=torch.float32).view(1, 1, 8)
print(F.lp_pool1d(input_data, 2, kernel_size=4, stride=2))
print(F.lp_pool1d(input_data, 2, kernel_size=4, stride=2, ceil_mode=True))