'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
import torch
input = torch.randn(1, 1, 2, 2, 2)
padding = (1, 1, 1, 1, 1, 1)
value = 0
output = torch.nn.ConstantPad3d(padding, value)(input)
print(output)