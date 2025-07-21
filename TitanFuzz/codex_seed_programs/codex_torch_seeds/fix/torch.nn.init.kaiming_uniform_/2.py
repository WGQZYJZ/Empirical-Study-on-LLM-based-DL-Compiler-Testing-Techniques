"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_uniform_\ntorch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import numpy as np
import torch
input_size = 10
output_size = 20
tensor = torch.zeros(input_size, output_size)
torch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(tensor)
print(tensor.shape)
print(tensor.dtype)
print(tensor.device)
print(tensor.layout)
print(tensor.mean())
print(tensor.std())
print(tensor.var())