'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ModuleDict\ntorch.nn.ModuleDict(modules=None)\n'
import torch
modules_dict = {'linear1': torch.nn.Linear(10, 20), 'linear2': torch.nn.Linear(20, 30)}
module_dict = torch.nn.ModuleDict(modules_dict)
print(module_dict)
print(list(module_dict.keys()))
print(list(module_dict.values()))
print(list(module_dict.items()))
print(list(module_dict.parameters()))