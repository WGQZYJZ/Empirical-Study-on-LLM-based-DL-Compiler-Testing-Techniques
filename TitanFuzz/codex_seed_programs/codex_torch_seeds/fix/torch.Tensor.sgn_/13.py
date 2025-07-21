'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn_\ntorch.Tensor.sgn_(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.float32)
print('Input Tensor: {}'.format(_input_tensor))
print('Signum of the input tensor: {}'.format(_input_tensor.sgn_()))