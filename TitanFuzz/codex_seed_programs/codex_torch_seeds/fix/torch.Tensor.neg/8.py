'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor: ', _input_tensor)
result = _input_tensor.neg()
print('Result: ', result)