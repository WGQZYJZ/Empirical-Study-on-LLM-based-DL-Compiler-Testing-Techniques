'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.prod(_input_tensor, dim=1, keepdim=True)
print('Output tensor: ', _output_tensor)