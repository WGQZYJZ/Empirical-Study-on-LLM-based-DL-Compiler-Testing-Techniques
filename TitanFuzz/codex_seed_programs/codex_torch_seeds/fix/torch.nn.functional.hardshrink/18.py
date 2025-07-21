'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ')
print(input_data)
output_data = torch.nn.functional.hardshrink(input_data)
print('Output data: ')
print(output_data)