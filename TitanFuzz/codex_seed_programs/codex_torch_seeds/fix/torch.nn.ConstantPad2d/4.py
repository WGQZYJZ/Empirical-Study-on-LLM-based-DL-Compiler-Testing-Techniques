'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.tensor([[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])
pad = nn.ConstantPad2d((2, 2, 2, 2), 0)
output = pad(input)
print(output)