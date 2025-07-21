'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eq\ntorch.Tensor.eq(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 3)
other_tensor = torch.randn(3, 3)
output_tensor = input_tensor.eq(other_tensor)
print('input_tensor:\n', input_tensor)
print('other_tensor:\n', other_tensor)
print('output_tensor:\n', output_tensor)