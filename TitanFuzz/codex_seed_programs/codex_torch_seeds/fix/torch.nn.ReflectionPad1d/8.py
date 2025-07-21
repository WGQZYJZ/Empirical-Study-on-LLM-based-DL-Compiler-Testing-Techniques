'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad1d\ntorch.nn.ReflectionPad1d(padding)\n'
import torch
import torch.nn as nn
input_data = torch.arange(1, 9, dtype=torch.float).view(1, 1, 8)
reflection_pad1d = nn.ReflectionPad1d(2)
output = reflection_pad1d(input_data)
print(output)