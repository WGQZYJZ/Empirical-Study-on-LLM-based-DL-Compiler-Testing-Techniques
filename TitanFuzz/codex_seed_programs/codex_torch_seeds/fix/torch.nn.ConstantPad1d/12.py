'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
input_data = torch.tensor([[1, 2, 3, 4, 5]])
pad = ConstantPad1d(padding=(2, 3), value=0)
print(pad(input_data))