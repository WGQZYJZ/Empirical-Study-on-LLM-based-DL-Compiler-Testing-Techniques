'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.sinc\ntorch.special.sinc(input, *, out=None)\n'
import torch
input_data = torch.linspace((- 10), 10, steps=100)
output_data = torch.special.sinc(input_data)
print(input_data)
print(output_data)