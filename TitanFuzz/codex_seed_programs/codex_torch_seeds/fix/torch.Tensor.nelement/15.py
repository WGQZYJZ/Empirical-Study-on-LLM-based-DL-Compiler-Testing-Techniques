'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nelement\ntorch.Tensor.nelement(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = _input_tensor.nelement()
print('_input_tensor = ', _input_tensor)
print('_output_tensor = ', _output_tensor)