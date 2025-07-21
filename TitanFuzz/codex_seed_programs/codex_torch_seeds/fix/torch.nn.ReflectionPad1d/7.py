'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad1d\ntorch.nn.ReflectionPad1d(padding)\n'
import torch
input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]], dtype=torch.float)
pad = torch.nn.ReflectionPad1d(2)
output = pad(input)
print(output)