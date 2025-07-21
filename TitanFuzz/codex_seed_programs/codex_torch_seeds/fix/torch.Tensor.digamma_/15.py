'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma_\ntorch.Tensor.digamma_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
torch.Tensor.digamma_(input_tensor)
print('\ninput_tensor: ', input_tensor)
'\nTask 4: Call the API torch.digamma\ntorch.digamma(_input_tensor)\n'
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.digamma(input_tensor)
print('\ninput_tensor: ', input_tensor)
print('\noutput_tensor: ', output_tensor)