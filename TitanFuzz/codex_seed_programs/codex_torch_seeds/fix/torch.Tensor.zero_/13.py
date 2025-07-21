'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:', _input_tensor)
_result = torch.Tensor.zero_(_input_tensor)
print('Result tensor:', _result)