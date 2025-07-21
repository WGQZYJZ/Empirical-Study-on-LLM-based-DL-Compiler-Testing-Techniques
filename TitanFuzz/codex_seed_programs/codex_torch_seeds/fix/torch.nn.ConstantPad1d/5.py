'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
import torch
from torch.nn import ConstantPad1d
input_data = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print(input_data)
padding = (1, 2)
value = 0
constant_pad1d = ConstantPad1d(padding, value)
output_data = constant_pad1d(input_data)
print(output_data)