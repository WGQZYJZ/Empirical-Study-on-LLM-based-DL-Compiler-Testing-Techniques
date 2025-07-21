'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.has_torch_function\ntorch.overrides.has_torch_function()\n'
import torch
input_data = torch.randn(1, 1, 2, 2)
print(torch.overrides.has_torch_function(input_data))