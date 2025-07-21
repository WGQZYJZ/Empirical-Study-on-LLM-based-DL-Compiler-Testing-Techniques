'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('input_tensor:')
print(input_tensor)
torch.Tensor.neg_(input_tensor)
print('\ninput_tensor after calling torch.Tensor.neg_:')
print(input_tensor)
input_tensor = torch.rand(3, 3)
print('\ninput_tensor:')
print(input_tensor)
output_tensor = torch.Tensor.neg(input_tensor)
print('\noutput_tensor:')
print(output_tensor)