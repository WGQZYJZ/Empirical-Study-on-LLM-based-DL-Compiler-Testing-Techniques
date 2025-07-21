'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad1d\ntorch.nn.ReflectionPad1d(padding)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8], dtype=torch.float32)
input_data = input_data.view(1, 1, 8)
reflection_pad_1d = nn.ReflectionPad1d(2)
output = reflection_pad_1d(input_data)
print('Input is ', input_data)
print('Output is ', output)