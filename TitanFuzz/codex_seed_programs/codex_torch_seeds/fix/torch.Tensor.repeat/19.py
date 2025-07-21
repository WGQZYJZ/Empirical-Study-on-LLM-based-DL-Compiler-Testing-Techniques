'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat\ntorch.Tensor.repeat(_input_tensor, *sizes)\n'
import torch
_input_tensor = torch.arange(1, 6)
print('Input tensor: ', _input_tensor)
print('Repeat input tensor: ', _input_tensor.repeat(2, 3))