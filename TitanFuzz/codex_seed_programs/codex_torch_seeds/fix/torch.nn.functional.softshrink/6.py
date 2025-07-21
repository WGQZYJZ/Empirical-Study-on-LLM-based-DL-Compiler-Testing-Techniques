'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
input_data = torch.randn(5, 10)
print('Input data: ', input_data)
output_data = torch.nn.functional.softshrink(input_data)
print('Output data: ', output_data)