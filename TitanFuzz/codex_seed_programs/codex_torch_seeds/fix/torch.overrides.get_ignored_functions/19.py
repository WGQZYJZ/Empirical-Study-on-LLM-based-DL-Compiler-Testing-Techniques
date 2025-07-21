'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.get_ignored_functions\ntorch.overrides.get_ignored_functions()\n'
import torch
input_data = torch.rand(1, 3, 224, 224)
ignored_functions = torch.overrides.get_ignored_functions()
print(ignored_functions)