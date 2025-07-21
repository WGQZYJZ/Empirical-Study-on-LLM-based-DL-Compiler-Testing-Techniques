'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad3d\ntorch.nn.ReflectionPad3d(padding)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.arange(1, 9, dtype=torch.float).view(1, 1, 2, 2, 2)
print('Input data is: ')
print(input_data)
reflection_pad3d = nn.ReflectionPad3d((1, 1, 1, 1, 1, 1))
output_data = reflection_pad3d(input_data)
print('Output data is: ')
print(output_data)
print('Output data is: ')
print(output_data)
print('Output data size is: ')
print(output_data.size())