'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Mish\ntorch.nn.Mish(inplace=False)\n'
import torch
from torch.nn import Mish
input_data = torch.randn(2, 2)
mish = Mish(inplace=False)
output = mish(input_data)
print(output)
'\nTask 4: Call the API torch.nn.functional.mish\ntorch.nn.functional.mish(input, inplace=False)\n'
import torch
from torch.nn.functional import mish
input_data = torch.randn(2, 2)
output = mish(input_data)
print(output)