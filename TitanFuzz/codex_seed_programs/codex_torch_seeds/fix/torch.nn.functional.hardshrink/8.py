'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(10)
print(input_data)
output_data = F.hardshrink(input_data, lambd=0.5)
print(output_data)