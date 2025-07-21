'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
import torch
input = torch.arange(1, 9, dtype=torch.float32).view(1, 2, 4).repeat(1, 1, 1)
print('Input:', input)
output = torch.nn.ConstantPad1d((1, 2), 0)(input)
print('Output:', output)