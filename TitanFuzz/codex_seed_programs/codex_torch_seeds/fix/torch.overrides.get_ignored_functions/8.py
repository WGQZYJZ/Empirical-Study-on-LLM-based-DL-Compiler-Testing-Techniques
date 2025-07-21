'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.get_ignored_functions\ntorch.overrides.get_ignored_functions()\n'
import torch
input_data = torch.rand(4, 3)
print(input_data)
print(torch.overrides.get_ignored_functions())