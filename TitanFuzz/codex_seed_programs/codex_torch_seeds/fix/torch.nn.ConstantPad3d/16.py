'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
from torch.nn import ConstantPad3d
input = torch.tensor([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
pad = ConstantPad3d(padding=(1, 1, 1, 1, 1, 1), value=0)
output = pad(input)
print(output)