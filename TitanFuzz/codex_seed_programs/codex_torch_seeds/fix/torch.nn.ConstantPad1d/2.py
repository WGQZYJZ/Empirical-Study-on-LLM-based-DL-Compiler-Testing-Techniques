'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.nn import ConstantPad1d
import torch
from torch.nn import ConstantPad1d
input = torch.tensor([[1, 2, 3, 4]])
print('Input: ', input)
output = ConstantPad1d((1, 1), 0)(input)
print('Output: ', output)