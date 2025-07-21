'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
from torch.nn import ConstantPad3d
input_data = torch.randn(1, 1, 3, 3, 3)
print(input_data)
pad = ConstantPad3d(padding=(1, 1, 1, 1, 1, 1), value=0)
output = pad(input_data)
print(output)