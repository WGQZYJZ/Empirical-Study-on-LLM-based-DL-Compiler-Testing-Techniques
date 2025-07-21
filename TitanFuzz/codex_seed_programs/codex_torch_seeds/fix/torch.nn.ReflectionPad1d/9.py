'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad1d\ntorch.nn.ReflectionPad1d(padding)\n'
import torch
import torch.nn as nn
input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8]]], dtype=torch.float32)
pad = nn.ReflectionPad1d(padding=2)
output = pad(input)
print(output)