"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
import torch
input_data = torch.arange(1, 11, dtype=torch.float32).view(1, 1, 10)
print('input_data:', input_data)
output = torch.nn.functional.pad(input_data, [2, 3], mode='constant', value=0)
print('output:', output)
print('output shape:', output.shape)