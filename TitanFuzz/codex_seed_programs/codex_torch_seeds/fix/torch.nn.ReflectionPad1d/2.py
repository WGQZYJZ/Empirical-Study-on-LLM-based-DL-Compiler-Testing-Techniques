'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad1d\ntorch.nn.ReflectionPad1d(padding)\n'
import torch
from torch.nn import ReflectionPad1d
input_data = torch.arange(1, 9, dtype=torch.float32).view(1, 1, 8)
print(input_data)
reflection_pad = ReflectionPad1d(3)
output_data = reflection_pad(input_data)
print(output_data)