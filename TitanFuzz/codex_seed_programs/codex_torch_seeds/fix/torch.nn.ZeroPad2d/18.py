'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
from torch.nn import ZeroPad2d
input_tensor = torch.tensor([[[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]])
zero_pad = ZeroPad2d(padding=(2, 3))
output_tensor = zero_pad(input_tensor)
print(output_tensor)