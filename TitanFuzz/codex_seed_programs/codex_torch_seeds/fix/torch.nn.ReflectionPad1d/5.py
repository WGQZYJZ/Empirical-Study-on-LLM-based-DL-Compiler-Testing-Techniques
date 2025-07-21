'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad1d\ntorch.nn.ReflectionPad1d(padding)\n'
import torch
input_data = torch.arange(1, 9, dtype=torch.float).view(1, 2, 4)
print('Input: \n', input_data)
reflection_pad = torch.nn.ReflectionPad1d(2)
output_data = reflection_pad(input_data)
print('Output: \n', output_data)