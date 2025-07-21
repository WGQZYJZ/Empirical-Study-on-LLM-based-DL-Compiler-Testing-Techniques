'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
from torch.nn import ConstantPad3d
input_data = torch.randn(1, 1, 4, 4, 4)
pad_size = (1, 1, 1, 1, 1, 1)
value = 1
output_data = ConstantPad3d(pad_size, value)(input_data)
print(output_data)