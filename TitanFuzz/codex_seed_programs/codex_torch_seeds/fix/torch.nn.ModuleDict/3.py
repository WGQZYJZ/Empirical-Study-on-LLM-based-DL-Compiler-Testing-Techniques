'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ModuleDict\ntorch.nn.ModuleDict(modules=None)\n'
import torch
input_data = torch.randn(2, 3, 4)
print(torch.__version__)
print(input_data)
module_dict = torch.nn.ModuleDict({'conv1': torch.nn.Conv2d(3, 4, 3), 'conv2': torch.nn.Conv2d(4, 5, 3)})
print(module_dict)
print(module_dict['conv1'])
print(module_dict.conv1)
print(module_dict.keys())
print(module_dict.values())
print(module_dict.items())
module_dict.update({'conv3': torch.nn.Conv2d(5, 6, 3)})
print(module_dict)