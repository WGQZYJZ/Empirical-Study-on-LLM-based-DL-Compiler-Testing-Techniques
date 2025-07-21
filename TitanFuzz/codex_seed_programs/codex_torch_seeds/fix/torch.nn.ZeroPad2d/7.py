'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
input = torch.randn(3, 3, 3)
print(input)
padding = (1, 1, 1, 1)
output = torch.nn.ZeroPad2d(padding)(input)
print(output)