'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn_\ntorch.Tensor.sgn_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _input_tensor.sgn_())