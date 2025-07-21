'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn_\ntorch.Tensor.sgn_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, requires_grad=True)
print('input_tensor:')
print(input_tensor)
print('output:')
print(input_tensor.sgn_())