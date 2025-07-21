'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
input_tensor = torch.randn(1, 1, 4, 4)
print('Input tensor: \n', input_tensor)
padding = (1, 1, 1, 1)
zero_pad = torch.nn.ZeroPad2d(padding)
output_tensor = zero_pad(input_tensor)
print('Output tensor: \n', output_tensor)