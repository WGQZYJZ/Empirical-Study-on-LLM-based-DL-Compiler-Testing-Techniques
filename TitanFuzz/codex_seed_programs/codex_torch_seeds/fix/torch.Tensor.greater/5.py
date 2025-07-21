'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater\ntorch.Tensor.greater(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: ', _input_tensor)
_result = torch.Tensor.greater(_input_tensor, 0)
print('Result: ', _result)