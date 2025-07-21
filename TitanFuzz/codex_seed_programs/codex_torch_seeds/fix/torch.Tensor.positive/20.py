'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3)
print('Input Tensor: ', _input_tensor)
print('Positive Tensor: ', _input_tensor.positive())