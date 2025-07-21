'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.float_power\ntorch.float_power(input, exponent, *, out=None)\n'
import torch
input_data = torch.rand(2, 3, 4)
output = torch.float_power(input_data, 2)
print(output)