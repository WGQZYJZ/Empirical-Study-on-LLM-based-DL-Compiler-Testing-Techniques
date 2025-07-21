'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ModuleDict\ntorch.nn.ModuleDict(modules=None)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('\nTask 2: Generate input data')
input_data = torch.randn(4, 3)
print('input_data: {}'.format(input_data))
print('\nTask 3: Call the API torch.nn.ModuleDict')
module_dict = nn.ModuleDict({'conv_1': nn.Conv2d(3, 10, kernel_size=5), 'conv_2': nn.Conv2d(10, 20, kernel_size=5)})
print('module_dict: {}'.format(module_dict))
print('\nTask 4: Call the API torch.nn.ModuleDict.get_item')
print("module_dict['conv_1']: {}".format(module_dict['conv_1']))