'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
_input_tensor = torch.randn(4, 3)
_output_tensor = _input_tensor.remainder_(divisor=2)
print('The output tensor is: ', _output_tensor)