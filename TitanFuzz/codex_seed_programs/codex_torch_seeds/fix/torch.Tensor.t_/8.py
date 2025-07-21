'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t_\ntorch.Tensor.t_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('input = ', _input_tensor)
print('output = ', _input_tensor.t_())