'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.square(input_data)
print(output_data)
'\nTask 4: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
output_data = torch.sqrt(input_data)
print(output_data)
'\nTask 5: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
output_data = torch.rsqrt(input_data)
print(output_data)
'\nTask 6: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
output_data = torch.pow