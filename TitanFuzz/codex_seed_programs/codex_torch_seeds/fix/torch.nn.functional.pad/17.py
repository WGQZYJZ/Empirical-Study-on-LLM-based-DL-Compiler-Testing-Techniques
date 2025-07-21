"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
input = torch.arange(1, 5, dtype=torch.float32).reshape(1, 1, 2, 2)
print('input: ', input)
pad = [1, 1, 1, 1]
mode = 'constant'
value = 0.0
output = torch.nn.functional.pad(input, pad, mode=mode, value=value)
print('output: ', output)