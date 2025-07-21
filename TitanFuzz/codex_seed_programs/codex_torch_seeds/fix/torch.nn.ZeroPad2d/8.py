'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
from torch.nn import ZeroPad2d
input_tensor = torch.randn(1, 1, 3, 3)
print(input_tensor)
padding = (1, 1, 1, 1)
output_tensor = ZeroPad2d(padding)(input_tensor)
print(output_tensor)