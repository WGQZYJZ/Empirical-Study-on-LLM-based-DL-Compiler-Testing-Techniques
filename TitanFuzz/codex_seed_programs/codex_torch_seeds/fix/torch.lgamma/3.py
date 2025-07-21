'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data:', input_data)
output_data = torch.lgamma(input_data)
print('Output data:', output_data)
output_data = torch.digamma(input_data)
print('Output data:', output_data)
output_data = torch.polygamma(1, input_data)
print('Output data:', output_data)
output_data = torch.erf(input_data)
print('Output data:', output_data)