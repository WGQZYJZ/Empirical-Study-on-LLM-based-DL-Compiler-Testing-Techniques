'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_warn_always_enabled\ntorch.is_warn_always_enabled()\n'
import torch
input_data = torch.rand(1, 1, 2, 3)
print(torch.is_warn_always_enabled())